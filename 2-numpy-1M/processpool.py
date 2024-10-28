# Multiprocessing pool (4 processes)
# Performance: 42 arrays/s on Python 3.12.7

import multiprocessing as mp
import numpy as np
import tqdm

process_count = 4
num_arrays = 30000

if __name__ == "__main__":
    pool = mp.Pool(processes=process_count)

    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        # essentially same as pool.map()
        for _ in (pool.apply(np.random.random, args=((100, 100, 10, 10),)) for _ in range(num_arrays)):
            pbar.update(1)
        pbar.close()
