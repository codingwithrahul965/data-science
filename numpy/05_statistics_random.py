import numpy as np

# 1. Random Number Generation
# Random floats between 0 and 1
rand_arr = np.random.rand(3, 3)
print("Random 3x3:\n", rand_arr)

# Standard Normal Distribution (mean=0, std=1)
randn_arr = np.random.randn(5)
print("\nStandard Normal:", randn_arr)

# Random Integers
rand_int = np.random.randint(1, 100, (2, 5))
print("\nRandom Integers (1-100):\n", rand_int)

# 2. Statistical Analysis
data = np.array([1, 2, 8, 4, 5, 9, 3])
print("\nData:", data)
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Percentile (75th):", np.percentile(data, 75))

# 3. Unique Elements
repeat_arr = np.array([1, 1, 2, 3, 3, 3, 4])
print("\nUnique Elements:", np.unique(repeat_arr))
