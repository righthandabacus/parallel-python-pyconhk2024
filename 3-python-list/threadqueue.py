# Mulththreading with a queue (4 threads)
# Performance: 11.33 arrays/s on Python 3.12.7
# Performance: 13.36 arrays/s on Python 3.13.0
# Performance: 5.95 arrays/s on Python 3.13.0t

import random
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
                [random.random() for _ in range(q)]
                for _ in range(p)
            ]
            for _ in range(n)
        ]
        for _ in range(m)
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
