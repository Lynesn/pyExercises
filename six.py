# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
wrd = input("Please enter a word:")
wrd = str(wrd)
rvs = wrd[::-1]
print(rvs)
if wrd == rvs:
    print("Yeay it's a palindrome")
else:
    print("Nope, this word is not a palindrome")
