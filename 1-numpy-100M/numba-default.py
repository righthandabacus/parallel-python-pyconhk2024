# Parallellization using numba with default settings
# Performance: 3.35 arrays/s on Python 3.12.7

import numba
import numpy as np
import tqdm

num_arrays = 300

@numba.njit()
def make_array():
    return np.random.random((100, 100, 100, 100))

for i in tqdm.trange(num_arrays, unit="arrays"):
    array = make_array()
