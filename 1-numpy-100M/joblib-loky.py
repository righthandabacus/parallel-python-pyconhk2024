# Using joblib with default loky backend. Observable launch overhead.
# Performance: 2.33 s/array = 0.43 array/s on Python 3.12.7

import numpy as np
import tqdm
from joblib import Parallel, delayed

process_count = 4   # -1 = auto
num_arrays = 300

if __name__ == "__main__":
    parallel = Parallel(n_jobs=process_count, return_as="generator")
    data = parallel(delayed(np.random.random)((100, 100, 100, 100)) for _ in range(num_arrays))

    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        for _ in data:
            pbar.update(1)
        pbar.close()
