# Using concurrent.futures.ProcessPoolExecutor
# Performance: 18.63 arrays/s on Python 3.12.7
# Performance: 19.70 arrays/s on Python 3.13.0
# Performance: 27.51 arrays/s on Python 3.13.0t

import concurrent.futures
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


process_count = 4   # -1 = auto
num_arrays = 300

if __name__ == "__main__":
    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar, \
         concurrent.futures.ProcessPoolExecutor(max_workers=process_count) as executor:
        jobs = (executor.submit(make_array, 100, 100, 10, 10) for _ in range(num_arrays))
        for future in concurrent.futures.as_completed(jobs):
            # memory alert: make sure to GC the `future` object ASAP
            array = future.result()
            pbar.update(1)
        pbar.close()
