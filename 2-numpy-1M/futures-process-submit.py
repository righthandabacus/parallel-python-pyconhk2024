# Using concurrent.futures.ProcessPoolExecutor
# Performance: 64 arrays/s on Python 3.12.7

import concurrent.futures
import numpy as np
import tqdm

process_count = 4   # -1 = auto
num_arrays = 30000

if __name__ == "__main__":
    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar, \
         concurrent.futures.ProcessPoolExecutor(max_workers=process_count) as executor:
        jobs = (executor.submit(np.random.random, (100, 100, 10, 10))
                for _ in range(num_arrays))
        for future in concurrent.futures.as_completed(jobs):
            # memory alert: make sure to GC the `future` object ASAP
            array = future.result()
            pbar.update(1)
        pbar.close()
