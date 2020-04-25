'''
Read in 10 numbers from the user. Place all 10 numbers into a list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

lista = []
lista1 = []
for i in range(10):
    lista.append(input('Enter a number: '))

for i in lista:
    if int(i) % 2 == 0:
        lista1.append(int(i))

for i in lista[::-1]:
    if int(i) % 2 != 0:
        lista1.append(int(i))
print(lista1)
