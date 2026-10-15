# my_list = [1, 2, 3]

# my_list.append(4)   # [1, 2, 3, 4]
# my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
# my_list.remove(2)   # [1, 99, 3, 4]
# my_list.pop()       # Removes last element -> [1, 99, 3]
# my_list.reverse()   # [3, 99, 1]
# my_list.sort()      # [1, 3, 99]

# print(my_list)  # Output: [1, 3, 99]

x = int(input("Enter a number: "))
squared = [x**2 for x in range(x)]
print(squared)  # Output: [0, 1, 4, 9, 16]