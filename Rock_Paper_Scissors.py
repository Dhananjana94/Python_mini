import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or q to quit the game: ").lower()

    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock:0, paper: 1, Scissor: 2

    computer_picked = options[random_number]
    print("Computer picked",computer_picked)

    if user_input =="rock" and computer_picked == "scissor":
        print("You Won")
        user_wins +=1



    elif user_input =="paper" and computer_picked == "rock":
        print("You Won")
        user_wins +=1



    elif user_input =="scissor" and computer_picked == "paper":
        print("You Won")
        user_wins +=1

    else:
        print("You Lost!")
        computer_wins +=1

print("You wins",user_wins,"times.")
print("Computer wins",computer_wins,"times.")
print("GoodBye!")