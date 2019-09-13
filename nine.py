# Generate a random a between 1 and 9 (including 1 and 9). Ask the user to guess the a, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

import random
a = random.randint(1, 9)
guess = 0
count = 0

while guess != a and guess != "exit":
    guess = input("What's your guess?")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < a:
        print("Too low!")
    elif guess > a:
        print("Too high!")
    else:
        print("Yeay! You got it!")
        print("And it only took you", count, "times!")
