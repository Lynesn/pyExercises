# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

num = input("please enter a number:")
a = num % 2
if a == 0:
    print("this number is even")
else:
    print("this number is odd")
