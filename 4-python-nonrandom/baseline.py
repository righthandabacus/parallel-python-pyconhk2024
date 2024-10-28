# Simple loop
# Performance: 7.80 arrays/s on Python 3.12.7
# Performance: 8.64 arrays/s on Python 3.13.0
# Performance: 6.24 arrays/s on Python 3.13.0t

import math
import tqdm

num_arrays = 300

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
