# Multiprocessing with a queue handled explicitly (4 processes)
# Performance: 104 arrays/s on Python 3.12.7

import multiprocessing as mp
import numpy as np
import tqdm

process_count = 4
num_each = 7500
queue = mp.Queue(3 * process_count)

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
    processes = []
    for _ in range(process_count):
        process = mp.Process(target=producer, args=(queue, num_each))
        processes.append(process)
        process.start()

    process = mp.Process(target=consumer, args=(queue, num_each * process_count))
    processes.append(process)
    process.start()

    for process in processes:
        process.join()
