#! /usr/bin/python3
import time
import random
import sys

print("\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n")
print("\n\n\n\n\n\n\n\n\n\n")
name = input("\n\n\nWhat is your name?\n\n\n")
time.sleep(1)
print("\n\nWelcome, " + name + "!\n\n")
time.sleep(1)
    
while True:
    human = input("\n\n\nRock, paper, or scissors?\n\n")
    computerInt = random.randint(0, 2)
    if computerInt == 0:
        computerInt = "rock.\n\n"
    elif computerInt == 1:
        computerInt = "paper.\n\n"
    else:
        computerInt = "scissors.\n\n"

# If human chooses rock
    if human.upper() == "ROCK":
        print("\n\nYou have chosen rock.\n\n\n\n\n")
        time.sleep(1)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Shoot!\n\n")
        time.sleep(1)
        print("The computer chooses " + str(computerInt))
        time.sleep(1)
        if computerInt == "rock.\n\n":
            print("It's a tie\n\n")
            time.sleep(2)
        if computerInt == "paper.\n\n":
            print("The computer wins.\n\n")
            time.sleep(2)
        if computerInt == "scissors.\n\n":
            print("You win, " + name + "!\n\n")
            time.sleep(2)
            
# If human chooses paper
    if human.upper() == "PAPER":
        print("\n\nYou have chosen paper.\n\n\n\n\n")
        time.sleep(1)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Shoot!\n\n")
        time.sleep(1)
        print("The computer chooses " + str(computerInt))
        time.sleep(1)
        if computerInt == "rock.\n\n":
            print("You win, " + name + "!\n\n")
            time.sleep(2)
        if computerInt == "paper.\n\n":
            print("It's a tie\n\n")
            time.sleep(2)
        if computerInt == "scissors.\n\n":
            print("The computer wins.\n\n")
            time.sleep(2)

# If human chooses scissors
    if human.upper() == "SCISSORS":
        print("\n\nYou have chosen scissors.\n\n\n\n\n")
        time.sleep(1)
        print("Rock!\n\n")
        time.sleep(1)
        print("Paper!\n\n")
        time.sleep(1)
        print("Scissors!\n\n")
        time.sleep(1)
        print("Shoot!\n\n")
        time.sleep(1)
        print("The computer chooses " + str(computerInt))
        time.sleep(1)
        if computerInt == "rock.\n\n":
            print("The computer wins.\n\n")
            time.sleep(2)
        if computerInt == "paper.\n\n":
            print("You win, " + name + "!\n\n")
            time.sleep(2)
        if computerInt == "scissors.\n\n":
            print("It's a tie\n\n")
            time.sleep(2)

# Restart game
    human = input("Would you like to play again? (y/n)\n\n")
    if not human == "y":
        print("Exiting game.\n\n")
        print("Thank you for playing!\n\n")
        time.sleep(1)
        break
