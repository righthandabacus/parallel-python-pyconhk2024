# Paralellization using numba
# Performance: 514.17 arrays/s on Python 3.12.7

import random
import numba
import numpy as np
import tqdm

num_arrays = 300

@numba.njit(parallel=True)
def make_array(m, n, p, q):
    result = np.empty((m, n, p, q))
    for i in numba.prange(m):
        for j in numba.prange(n):
            for k in numba.prange(p):
                for h in numba.prange(q):
                    result[i, j, k, h] = random.random()
    return result

for i in tqdm.trange(num_arrays, unit="arrays"):
    array = make_array(100, 100, 10, 10)
