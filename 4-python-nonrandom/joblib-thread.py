# Using joblib with threading backend.
# Performance: 7.00 arrays/s on Python 3.12.7
# Performance: 8.03 arrays/s on Python 3.13.0
# Performance: 21.04 arrays/s on Python 3.13.0t

import math
import tqdm
from joblib import Parallel, delayed


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


process_count = 4   # -1 = auto
num_arrays = 300

if __name__ == "__main__":
    parallel = Parallel(n_jobs=process_count, return_as="generator", prefer="threads")
    data = parallel(delayed(make_array)(100, 100, 10, 10) for _ in range(num_arrays))

    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        for _ in data:
            pbar.update(1)
        pbar.close()
