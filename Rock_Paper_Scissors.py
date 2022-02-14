import random

user_wins = 0
computer_wins = 0

options = ["Rock","Paper","Scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or q to quit the game ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock:0, paper: 1, Scissor: 2

    computer_picked = options[random_number]
    print("Computer picked",computer_picked)


print("GoodBye!")