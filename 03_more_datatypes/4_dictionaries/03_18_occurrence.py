'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

unos = 'Write a script that takes a string from the user'
unos = unos.lower()
brojac = 1
recnik = {}
for i in unos:
    if i in recnik.keys():
        recnik[i] = recnik[i] + 1
        brojac += 1
    else:
        recnik[i] = 1

print('Letters occurence:', recnik.items())
