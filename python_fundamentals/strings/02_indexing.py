
#we cannot modify a string because strings are immutable. This means that once a string is created, it cannot be changed. If we try to change a character in a string, we will get an error.


name = "Harry" 

# name = "H   a   r  r   y"
#         0   1   2  3   4
#        -5  -4  -3 -2  -1

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4]) # name[-4+5] name[1]
print(name[-5])

