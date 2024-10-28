# Simple loop
# Performance: 2.52 array/s

import numpy as np
import tqdm

num_arrays = 300

for i in tqdm.trange(num_arrays, unit="arrays"):
    array = np.random.random((100, 100, 100, 100))
