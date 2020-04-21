'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel in the string and print a count for each of them?

'''
sentence = (input('Enter a sentence: '))
vowels = ['a', 'o', 'e', 'i', 'u']
count = 0
for i in sentence:
    if i in vowels:
        count += 1

print(f'There are {count} vowels in a sentence.')

##### Challenge ######

sentence = (input('Enter a sentence: '))
vowels = ['a', 'o', 'e', 'i', 'u']
vowels2 = {}
for i in sentence:
    if i in vowels:
        if i in vowels2:
            vowels2[i] += 1
        else:
            vowels2[i] = 1
print(sorted(vowels2.items(), key=lambda kv: kv[1], reverse=True))
