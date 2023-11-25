# Rock, Paper, Scissors game

import random

print("Rock, Paper, Scissors")

# available options
options = ["rock", "paper", "scissors"]

while True:
    print("Enter choice \n1 for rock \n2 for paper \n3 for scissors \n0 for quit")
    
    # get player's choice
    choice = int(input("Your turn: "))
    
    # quit the game if player enters 0
    if choice == 0:
        print("Bye!")
        break
    elif choice > 3:
        print("Invalid input. Try again.")
        continue

    # get computer's choice
    comp_choice = random.choice(options)
    print("Computer chose ", comp_choice)

    # determine the winner
    if choice == 1 and comp_choice == "rock":
        print("Tie!")
    elif choice == 1 and comp_choice == "paper":
        print("You lose!", comp_choice, "covers", "rock")
    elif choice == 1 and comp_choice == "scissors":
        print("You win!", "rock", "smashes", comp_choice)
    elif choice == 2 and comp_choice == "rock":
        print("You win!", "paper", "covers", comp_choice)
    elif choice == 2 and comp_choice == "paper":
        print("Tie!")
    elif choice == 2 and comp_choice == "scissors":
        print("You lose!", comp_choice, "cut", "paper")
    elif choice == 3 and comp_choice == "rock":
        print("You lose!", comp_choice, "smashes", "scissors")
    elif choice == 3 and comp_choice == "paper":
        print("You win!", "scissors", "cut", comp_choice)
    elif choice == 3 and comp_choice == "scissors":
        print("Tie!")
