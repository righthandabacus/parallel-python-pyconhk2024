# Using concurrent.futures.ThreadPoolExecutor
# Performance: 255 arrays/s on Python 3.12.7

import concurrent.futures
import numpy as np
import tqdm

process_count = 4   # -1 = auto
num_arrays = 30000

if __name__ == "__main__":
    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar, \
         concurrent.futures.ThreadPoolExecutor(max_workers=process_count) as executor:
        for result in executor.map(np.random.random, ((100, 100, 10, 10) for _ in range(num_arrays))):
            pbar.update(1)
        pbar.close()
