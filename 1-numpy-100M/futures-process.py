# Using concurrent.futures.ProcessPoolExecutor
# Performance: 2.85 s/array = 0.35 array/s on Python 3.12.7

import concurrent.futures
import numpy as np
import tqdm

process_count = 4   # -1 = auto
num_arrays = 300

if __name__ == "__main__":
    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar, \
         concurrent.futures.ProcessPoolExecutor(max_workers=process_count) as executor:
        for result in executor.map(np.random.random, ((100, 100, 100, 100) for _ in range(num_arrays))):
            pbar.update(1)
        pbar.close()
