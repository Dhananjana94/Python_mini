import random

numbrInRange = input("Plese enter a number : ")

if numbrInRange.isdigit():
    numbrInRange = int(numbrInRange)

    if numbrInRange <= 0:
        print("Plese enter number greater than 0: ")
        quit()

else:
    print("Please enter the number")
    quit()

randomNumber = random.randint(0,numbrInRange) #we need to add start number here

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter the number")
        continue

    if user_guess == numbrInRange:
        print("Your guess is correct ")
        break

    elif user_guess > numbrInRange:
         print("Your number is greater than range")

    else:
        print("Your number is below the number")

print("You got it in ",guesses," guesses")