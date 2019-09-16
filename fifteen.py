# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

def phraseReverse(string):
    # we split the word/list first
    list1 = string.split(' ')
    #then we reverse it.  
    list1.reverse()
    # now we join them
    list1 = ' '.join(list1)
    # then retrn it
    return list1

question = input('Please enter a phrase: ')
answer = phraseReverse(question)
print(answer)
