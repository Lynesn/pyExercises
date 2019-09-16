# Write a program that asks the user how many Fibonnaci numbers to generate
# and then generates them. Take this opportunity to think about how y
# ou can use functions.


def fibo():
    num = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    elif num > 2:
        fib = [1, 1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
print(fibo())
input()
