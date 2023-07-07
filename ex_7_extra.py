#Скласти програму обчислення відстані між точками з координатами, що вводяться користувачем.

# Distance - sqrt((x2-x1)^2 + (y2-y1)^2)
# Enter coordinates...
from math import sqrt

x_1 = float(input('Enter x_1 :'))
x_2 = float(input('Enter x_2 :'))
y_1 = float(input('Enter y_1 :'))
y_2 = float(input('Enter y_2 :'))

distance = round(sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2), 3)

print(distance)
