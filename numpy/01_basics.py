import numpy as np

# 1. Creating Arrays
# From a list
arr = np.array([1, 2, 3, 4, 5])
print("Basic Array:", arr)

# 2. Attributes
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Data Type:", arr.dtype)
print("Size:", arr.size)

# 3. Specialized Arrays
zeros = np.zeros((3, 3))
print("\nZeros Matrix:\n", zeros)

ones = np.ones((2, 4))
print("\nOnes Matrix:\n", ones)

identity = np.eye(3)
print("\nIdentity Matrix:\n", identity)

# 4. Range-based creation
range_arr = np.arange(0, 10, 2)
print("\nArange (0 to 10 step 2):", range_arr)

linspace_arr = np.linspace(0, 1, 5)
print("Linspace (0 to 1 with 5 points):", linspace_arr)
