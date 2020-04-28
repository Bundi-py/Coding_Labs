'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
var = int(input('Enter a number 1-12: '))
if var < 12:
    if var == 1:
        print("January")
    if var == 2:
        print("February")
    elif var == 3:
        print("March")
    elif var == 4:
        print("April")
    elif var == 5:
        print("May")
    elif var == 6:
        print("June")
    elif var == 7:
        print("July")
    elif var == 8:
        print("August")
    elif var == 9:
        print("September")
    elif var == 10:
        print("October")
    elif var == 11:
        print("November")
    elif var == 12:
        print("December")
else:
    print("Other")

print("Good bye!")
