'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''
broj1 = int(input('Enter a lower number in the range from 1 to 100: '))
broj2 = int(input('Enter a higher number in the range from 1 to 100: '))

zbir = 0
for i in range(broj1, broj2 + 1):
    zbir += i
print('Sum of all numbers between lower and higher is', zbir)
