# Multiprocessing thread pool (4 processes)
# Performance: 12.85 arrays/s on Python 3.12.7
# Performance: 15.18 arrays/s on Python 3.13.0
# Performance: 10.77 arrays/s on Python 3.13.0t

import multiprocessing as mp
import multiprocessing.pool
import random
import tqdm

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

process_count = 4
num_arrays = 300

if __name__ == "__main__":
    with mp.pool.ThreadPool(processes=process_count) as pool, \
         tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        # essentially same as pool.map()
        for _ in (pool.apply(make_array, args=(100, 100, 10, 10)) for _ in range(num_arrays)):
            pbar.update(1)
        pbar.close()
