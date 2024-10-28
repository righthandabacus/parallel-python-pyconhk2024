# Multiprocessing with a queue handled explicitly (4 processes)
# Performance: 18.58 array/s on Python 3.12.7
# Performance: 20.32 array/s on Python 3.13.0
# Performance: 26.65 array/s on Python 3.13.0t

import multiprocessing as mp
import random
import tqdm

process_count = 4
num_each = 75
queue = mp.Queue(3 * process_count)


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