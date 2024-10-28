# Using concurrent.futures.ProcessPoolExecutor
# Performance: 19.21 arrays/s on Python 3.12.7
# Performance: 20.15 arrays/s on Python 3.13.0
# Performance: 27.10 arrays/s on Python 3.13.0t

import concurrent.futures
import random
import tqdm


def make_array(dims):
    m, n, p, q = dims
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


process_count = 4   # -1 = auto
num_arrays = 300

if __name__ == "__main__":
    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar, \
         concurrent.futures.ProcessPoolExecutor(max_workers=process_count) as executor:
        for result in executor.map(make_array, ((100, 100, 10, 10) for _ in range(num_arrays))):
            pbar.update(1)
        pbar.close()
