'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
integer = 24
print(float(integer))

float_num = 56.42
print(int(float_num))

print(float_num // integer)

fist_number = (input('Enter the fist number: '))
second_number = (input('Enter the second number: '))

print(int(fist_number) * int(second_number))
