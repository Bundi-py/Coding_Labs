'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

unos = input('Enter some text with a few words repeated: ')
unos = unos.lower().split()
brojac = 1
recnik = {}
for i in unos:
    if i in recnik.keys():
        recnik[i] = recnik[i] + 1
        brojac += 1
    else:
        recnik[i] = 1

print('The most frequent word is:', sorted(
    recnik, key=recnik.get, reverse=True)[:1])
