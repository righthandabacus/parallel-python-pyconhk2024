# Simple loop
# Performance: 272 arrays/s

import numpy as np
import tqdm

num_arrays = 30000

for i in tqdm.trange(num_arrays, unit="arrays"):
    array = np.random.random((100, 100, 10, 10))
