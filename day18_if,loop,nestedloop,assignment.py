print("Welcome to Guess a Number ")

print()
print("Guess a number between 0 and 20")
print()

print("Lets Play")

firstNumber = 18
attempt = 0

while True:
    user_guess = int(input("Guess a number?"))

    if user_guess < 0:
        print("Please guess a number between 0 and 20")
        attempt += 1
        continue
    elif user_guess < firstNumber:
        print("Your guess is toolow")
        attempt += 1
        continue

    elif user_guess >= 15 and user_guess <= 20 and user_guess != 18:
        print("You are close")
        attempt += 1
        continue

    elif user_guess == firstNumber:
        print("You are right.Horaay!!")
        break
    else:
        print("Is that even a number??")

print("You have made ", attempt, "attempts to get to the right answer.")
