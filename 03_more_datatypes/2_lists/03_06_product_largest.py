'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
lista = []
for i in range(10):
    lista.append(input('Enter a number: '))
print('The largest number is:', max(lista))

##########

product = 1
for n in lista:
    product *= int(n)
print('Product of numbers in the list is:', product)
