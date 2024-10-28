# Parallellization using numba with default settings
# Performance: 22.48 arrays/s on Python 3.12.7

import random
import numba
import tqdm

num_arrays = 300


@numba.njit()
def make_array(m, n, p, q):
    return [
        [
            [
                [random.random() for _ in range(q)]
                for _ in range(p)
            ]
            for _ in range(n)
        ]
        for _ in range(m)
    ]


for i in tqdm.trange(num_arrays, unit="arrays"):
    array = make_array(100, 100, 10, 10)
