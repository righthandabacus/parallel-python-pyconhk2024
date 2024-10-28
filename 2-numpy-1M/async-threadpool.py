# Using concurrent.futures.ThreadPoolExecutor
# Performance: 273 array/s on Python 3.12.7

import asyncio
import concurrent.futures
import numpy as np
import tqdm

process_count = 4   # -1 = auto
num_arrays = 30000

async def main():
    with tqdm.tqdm(total=num_arrays, unit="arrays") as pbar, \
         concurrent.futures.ThreadPoolExecutor(max_workers=process_count) as executor:
        futures = (loop.run_in_executor(executor, np.random.random, (100, 100, 10, 10))
                   for _ in range(num_arrays))
        for job in asyncio.as_completed(futures):
            result = await job
            pbar.update(1)
        pbar.close()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
