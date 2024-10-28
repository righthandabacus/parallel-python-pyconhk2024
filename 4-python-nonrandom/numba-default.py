# Parallellization using numba with default settings
# Performance: 20.93 arrays/s on Python 3.12.7

import math
import numba
import tqdm

num_arrays = 300


@numba.njit()
def make_array(m, n, p, q):
    return [
        [
            [
                [math.sin(i*j*k*h) for h in range(q)]
                for k in range(p)
            ]
            for j in range(n)
        ]
        for i in range(m)
    ]


for i in tqdm.trange(num_arrays, unit="arrays"):
    array = make_array(100, 100, 10, 10)
