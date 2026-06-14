import numpy as np

# 1. Basic Comparison
arr = np.array([10, 20, 30, 40, 50, 60])
mask = arr > 30
print("Array:", arr)
print("Mask (arr > 30):", mask)
print("Filtered Data:", arr[mask])

# 2. Multiple Conditions
# Use & (and), | (or), ~ (not)
# Note: You MUST use parentheses for logical operators
rich_mask = (arr > 20) & (arr < 50)
print("\nElements between 20 and 50:", arr[rich_mask])

# 3. np.where
# Change values based on a condition: np.where(condition, if_true, if_false)
new_arr = np.where(arr > 35, "High", "Low")
print("\nCategorized Data:", new_arr)

# 4. Modifying elements with masks
arr_copy = arr.copy()
arr_copy[arr_copy < 30] = 0
print("\nOriginal values < 30 replaced with 0:", arr_copy)

# 5. checking if any or all elements meet condition
print("\nAny elements > 55?", np.any(arr > 55))
print("All elements > 5?", np.all(arr > 5))
