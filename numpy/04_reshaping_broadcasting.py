import numpy as np

# 1. Reshaping
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print("Original 1D:\n", arr)
print("Reshaped to 3x4:\n", reshaped)

# 2. Flattening
print("\nFlattened:", reshaped.ravel())

# 3. Stacking (Joining)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nVertical Stack:\n", np.vstack((a, b)))
print("Horizontal Stack:", np.hstack((a, b)))

# 4. Broadcasting
# Adding a scalar to an array
# Adding a 1D array to a 2D array
matrix = np.zeros((3, 3))
row = np.array([1, 0, 1])
print("\nBroadcasting Addition:\n", matrix + row)
