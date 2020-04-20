'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
volume = round((3.14**2) * (3.14 * 5), 2)
surface = round((2 * 3.14 * 3.14 * 5) + (2 * 3.14 * 3.14**2), 2)
print(f'Volume of a cylindar is {volume} and surface is {surface}.')
