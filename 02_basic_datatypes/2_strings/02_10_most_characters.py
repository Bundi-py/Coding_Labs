'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit the script to print only the string with the most characters? You can look into the topic "Conditionals" to solve this challenge.

'''
string1 = (input('Enter text 1: '))
string2 = (input('Enter text 2: '))
string3 = (input('Enter text 3: '))

print(f'No. of characters: {len(string1)}, in the string: {string1}')
print(f'No. of characters: {len(string2)}, in the string: {string2}')
print(f'No. of characters: {len(string3)}, in the string: {string3}')

#### Challenge ####

string1 = (input('Enter text 1: '))
string2 = (input('Enter text 2: '))
string3 = (input('Enter text 3: '))

max = ''
if len(string1) > len(string2):
    max = string1
else:
    max = string2

if len(string3) > len(max):
    max = string3

print(f'No. of characters: {len(max)}, in the longest string: {max}')
