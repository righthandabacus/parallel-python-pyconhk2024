# Using joblib with threading backend.
# Performance: 257 arrays/s on Python 3.12.7

import numpy as np
import tqdm
from joblib import Parallel, delayed

process_count = 4   # -1 = auto
num_arrays = 30000

if __name__ == "__main__":
    parallel = Parallel(n_jobs=process_count, return_as="generator", prefer="threads")
    data = parallel(delayed(np.random.random)((100, 100, 10, 10)) for _ in range(num_arrays))

    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        for _ in data:
            pbar.update(1)
        pbar.close()
