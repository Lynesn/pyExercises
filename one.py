# Create a program that asks the user to enter their name and their 
# age. Print out a message addressed to them that tells them 
# the year that they will turn 100 years old.

from datetime import datetime
name = input("please enter your name:")
age = int(input("please enter your age:"))
year100 = int((100-age) + datetime.now().year)
print("Hello" + name + ","  "you will turn 100 years in", + year100)