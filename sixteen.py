# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

import random

user_input = int(input("How many characters long password do you need?"))
characters = "abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.:,?;<>#&@"

def password(a):
    output = []
    i = 1
    while i <= a:
        b = random.choice(characters)
        output.append(b)
        i += 1
    print("Your password: " + "".join(output))


password(user_input)
