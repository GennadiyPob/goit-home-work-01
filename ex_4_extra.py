'''
Дано радіус кола r (вводяться користувачем). Скласти програму знаходження довжини кола та площі кола

'''

# Довжина кола - 2*Pi*R
# Площа кола - (Pi*R^2)/2

from math import pi

radius = float(input('Enter radius : '))
length = round(2*pi*radius, 2)              #round is fix a 2 digits after point
square = round(((pi * radius ** 2)/2), 2)    

print(f'Radius : {radius}, Length : {length}, Square {square}')