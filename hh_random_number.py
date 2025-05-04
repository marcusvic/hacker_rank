import random

selected_number = round(random.random()*100, 0)

print("I'm thinking of a number between 1 and 100.")

guess = 0
counter = 0

while guess != selected_number:
    print("Take a guess:")
    guess = int(input())
    counter += 1
    if guess > selected_number:
        print("Too high!")
    elif guess < selected_number:
        print("Too low!")
    else:
        print(f"You got it in {counter} guesses!")
