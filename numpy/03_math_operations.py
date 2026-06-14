import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# 1. Element-wise operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Power:", a ** 2)

# 2. Universal Functions (ufuncs)
print("\nSquare Root:", np.sqrt(a))
print("Exponential:", np.exp(b))
print("Sine:", np.sin(a))

# 3. Aggregate Functions
print("\nSum:", a.sum())
print("Mean:", a.mean())
print("Max:", a.max())
print("Standard Deviation:", a.std())

# 4. Matrix Multiplication
c = np.array([[1, 2], [3, 4]])
d = np.array([[5, 6], [7, 8]])
print("\nMatrix Product:\n", np.dot(c, d)) # or c @ d
