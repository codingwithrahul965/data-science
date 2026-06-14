"""
WORKING OF ROCK PAPER SCISSOR GAME:

1- input  from user(rock,paper,scissor)
2- computer choice(rock,paper,scissor)
3- result print

cases:
A- rock
rock - rock = draw
rock - paper = paper win
rock - scissor = rock win

B- paper
paper - rock = paper win
paper - paper = draw
paper - scissor = scissor win

C- scissor
scissor - rock = rock win
scissor - paper = scissor win
scissor - scissor = draw

"""

import random
item_list = ['rock', 'paper', 'scissor']
user_choice = input("Enter your choice (rock, paper, scissor): ")
computer_choice = random.choice(item_list)
print(f"User choice: {user_choice}")
print(f"Computer choice: {computer_choice}")

#for printing result loops are using if-elif-else.

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Computer wins!")
    else:
        print("User wins!")
elif user_choice == "paper":
    if computer_choice == "scissor":
        print("Computer wins!")
    else:
        print("User wins!")
elif user_choice == "scissor":
    if computer_choice == "rock":
        print("Computer wins!")
    else:
        print("User wins!")