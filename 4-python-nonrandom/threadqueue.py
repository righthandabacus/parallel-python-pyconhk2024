# Mulththreading with a queue (4 threads)
# Performance: 7.41 arrays/s on Python 3.12.7
# Performance: 8.03 arrays/s on Python 3.13.0
# Performance: 18.87 arrays/s on Python 3.13.0t

import math
import queue
import threading
import tqdm

thread_count = 4
num_each = 75
queue = queue.Queue(3 * thread_count)

def make_array(m, n, p, q):
    return [
        [
            [
                [math.sin(i*j*k*h) for h in range(q)]
                for k in range(p)
            ]
            for j in range(n)
        ]
        for i in range(m)
    ]

def producer(queue, count):
    """Generate N numpy arrays and put to the queue"""
    for _ in range(count):
        array = make_array(100, 100, 10, 10)
        queue.put(array)

def consumer(queue, total):
    """Consume arrays from the queue"""
    for i in tqdm.trange(total, unit="arrays"):
        _ = queue.get()

if __name__ == "__main__":
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=producer, args=(queue, num_each))
        threads.append(thread)
        thread.start()

    thread = threading.Thread(target=consumer, args=(queue, num_each * thread_count))
    threads.append(thread)
    thread.start()

    for thread in threads:
        thread.join()
