# Parallellization using numba with default settings
# Performance: 373 arrays/s on Python 3.12.7

import numba
import numpy as np
import tqdm

num_arrays = 30000

@numba.njit()
def make_array():
    return np.random.random((100, 100, 10, 10))

for i in tqdm.trange(num_arrays, unit="arrays"):
    array = make_array()
