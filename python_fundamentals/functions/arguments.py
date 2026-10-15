# def add(a,b):
#     x=a+b
#     return x

# c=add(3,5)
# print(c)


def add(a,b,plus=0):
    x=a+b+plus
    return x

c=add(3,5,3)
print(c)

c1=add(b=5,a=7)
print(c1)