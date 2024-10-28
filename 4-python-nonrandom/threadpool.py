# Multiprocessing thread pool (4 processes)
# Performance: 7.76 arrays/s on Python 3.12.7
# Performance: 8.46 arrays/s on Python 3.13.0
# Performance: 6.28 arrays/s on Python 3.13.0t

import multiprocessing as mp
import multiprocessing.pool
import math
import tqdm

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

process_count = 4
num_arrays = 300

if __name__ == "__main__":
    with mp.pool.ThreadPool(processes=process_count) as pool, \
         tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        # essentially same as pool.map()
        for _ in (pool.apply(make_array, args=(100, 100, 10, 10)) for _ in range(num_arrays)):
            pbar.update(1)
        pbar.close()
