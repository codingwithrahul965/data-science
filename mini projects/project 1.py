import random
secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
attempts = 0
while guess != secret:
    if guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 10: "))
    attempts = attempts + 1
print("Congratulations! You guessed the number.")
print("attempts", attempts)