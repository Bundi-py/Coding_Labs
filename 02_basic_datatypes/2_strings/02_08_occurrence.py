'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
sentence = (input('Enter a sentence: '))
symbol = (input('Enter a letter from the sentence: '))
print('Result: ', sentence.find(symbol))
