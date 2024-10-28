# Using joblib with default loky backend. Observable launch overhead.
# Performance: 18.69 arrays/s on Python 3.12.7
# Performance: 19.34 arrays/s on Python 3.13.0
# Performance: 25.68 arrays/s on Python 3.13.0t

import random
import tqdm
from joblib import Parallel, delayed


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


process_count = 4   # -1 = auto
num_arrays = 300

if __name__ == "__main__":
    parallel = Parallel(n_jobs=process_count, return_as="generator")
    data = parallel(delayed(make_array)(100, 100, 10, 10) for _ in range(num_arrays))

    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar:
        for _ in data:
            pbar.update(1)
        pbar.close()
