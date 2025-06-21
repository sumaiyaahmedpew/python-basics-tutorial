# Copying arrays
import numpy as np
arr = np.array([1, 2, 3])
copy_arr = arr.copy()
copy_arr[0] = 100
print("Original:", arr)
print("Copy:", copy_arr)
