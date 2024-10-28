# Mulththreading with a queue (4 threads)
# Performance: 263 arrays/s on Python 3.12.7

import queue
import threading
import numpy as np
import tqdm

thread_count = 4
num_each = 7500
queue = queue.Queue(3 * thread_count)

def producer(queue, count):
    """Generate N numpy arrays and put to the queue"""
    for _ in range(count):
        array = np.random.random((100, 100, 10, 10))
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
