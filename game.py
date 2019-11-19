import random

entry = raw_input("Welcome to rock, paper, scissors. Please enter your value: ")
games = ['rock','paper','scissors']
choice = random.choice(games)
print ("My choice is " + choice)
if entry == choice:
    print ("Let's play again")
elif entry == "rock" and choice == "paper" or entry == "paper" and choice == "scissors" or entry == "scissors" and choice == "rock":
    print ("You lose.")
else:
    print ("You win")
