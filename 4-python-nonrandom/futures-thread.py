# Using concurrent.futures.ThreadPoolExecutor
# Performance: 7.15 arrays/s on Python 3.12.7
# Performance: 8.14 arrays/s on Python 3.13.0
# Performance: 18.84 arrays/s on Python 3.13.0t

import concurrent.futures
import math
import tqdm


def make_array(dims):
    m, n, p, q = dims
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


process_count = 4   # -1 = auto
num_arrays = 300

if __name__ == "__main__":
    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar, \
         concurrent.futures.ThreadPoolExecutor(max_workers=process_count) as executor:
        for result in executor.map(make_array, ((100, 100, 10, 10) for _ in range(num_arrays))):
            pbar.update(1)
        pbar.close()
