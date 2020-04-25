'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
input = "hello world"
lista = []
N = 2
for i in range(0, len(input)):
    lista.append(input[i])
res = tuple(input[i: i + N] for i in range(0, len(input), 2))
print(res)
