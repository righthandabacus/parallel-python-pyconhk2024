# Multiprocessing pool (4 processes)
# Performance: 2.56 s/array = 0.39 array/s on Python 3.12.7

import multiprocessing as mp
import numpy as np
import tqdm

process_count = 4
num_arrays = 300

if __name__ == "__main__":
    pool = mp.Pool(processes=process_count)

    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        # essentially same as pool.map()
        for _ in (pool.apply(np.random.random, args=((100, 100, 100, 100),)) for _ in range(num_arrays)):
            pbar.update(1)
        pbar.close()
