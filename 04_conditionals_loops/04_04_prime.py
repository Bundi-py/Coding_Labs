'''
Print out every prime number between 1 and 100.

'''
lista = []

for number in range(1, 101):
    count = 0
    for i in range(2, (number//2 + 1)):
        if number % i == 0:
            count += 1
            break
    if count == 0 and number != 1:
        lista.append(number)
print(lista)
