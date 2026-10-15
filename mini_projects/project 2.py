import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Enter the length of the password: "))
password=""
for i in range(length):
    password+=random.choice(chars)
print("generate password:",password)    