import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:\n", arr)

# 1. Basic Indexing
print("\nElement at (0, 0):", arr[0, 0])
print("Last element:", arr[-1, -1])

# 2. Slicing
# [rows, columns]
print("\nFirst two rows:\n", arr[:2, :])
print("Second column:\n", arr[:, 1])
print("Sub-matrix (2x2):\n", arr[0:2, 1:3])

# 3. Boolean Indexing (Filtering)
mask = arr > 5
print("\nElements > 5:", arr[mask])

# 4. Fancy Indexing
print("\nRows 0 and 2:\n", arr[[0, 2], :])
