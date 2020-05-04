# A simple Stone, Papers, Scissors game
import random as rd
import time

# instructions are above
print("Welcome to the game. You have 3 options to choose from, Rock, Papers or Scissors \n for Rock choose \"R\" \n"
      "For Paper choose \"P\" \n For Scissors, choose \"S\"")

#choice made by the player.
player_choice = input("Enter your choice:").upper()
if  player_choice== "R":
    print("You have selected Rock")
elif player_choice == "P":
    print("You have selected Paper")
elif player_choice == "S":
    print("You have selected Scissors")
else:
    print("INVALID SELECTION")
computer_options = ["R","P","S"]
computer_choice = rd.choice(computer_options)
print(" The computer has selected " + computer_choice)
time.sleep(1)

#if player chooses Rock or "R"
if player_choice == "R":
    if computer_choice == "P":
        print("You lose against Paper")
    elif computer_choice == "S":
        print("You have won against Scissors")
    else:
        print("It's a tie.")
# if player chooses papers or "p"
if player_choice == "P":
    if computer_choice == "S":
        print("You have lost against Scissors")
    elif computer_choice == "S":
        print("You have won against Paper")
    else:
        print("It's a tie")
#if player chooses Scissors or "s"
if player_choice == "S":
    if computer_choice == "R":
        print("You lose against Rock")
    elif computer_choice == "P":
        print("You win against Paper ")
    else:
        print("It's a tie")



