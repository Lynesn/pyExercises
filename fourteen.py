# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
def dup_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


print(dup_list([1, 2, 5, 9, 9, 1, 4, 5]))
