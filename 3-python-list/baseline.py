# Simple loop
# Performance: 12.98 arrays/s on Python 3.12.7
# Performance: 15.23 arrays/s on Python 3.13.0
# Performance: 11.41 arrays/s on Python 3.13.0t

import random
import tqdm

num_arrays = 300

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
