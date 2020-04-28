'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
lista = []
for i in range(101):
    if i % 2 == 1:
        lista.append(i)
print(lista)
