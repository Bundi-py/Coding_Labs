'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean


def div47(broj):
    if int(broj) % 4 == 0 or int(broj) % 7 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean


def div74(broj):
    if int(broj) % 4 == 0 and int(broj) % 7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000


def unos():
    a = int(input('Enter a number between 1 and 1,000,000,000: '))
    print(f'{a} entered.')

# call your functions, passing in the user input as the arguments, and set their output equal to new variables


def unos():
    a = int(input('Enter a number between 1 and 1,000,000,000: '))
    print(f'{a} entered.')
    ac = div47(a)
    ad = div74(a)
    # print your new variables to display the results
    print(ac)
    print(ad)


unos()
