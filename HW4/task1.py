# Вывести треугольник #1 с шириной N с помощью цикла while

width = int(input('Enter a width of a triangle: \n'))
symbol = '*'

while width != 0:
    print(symbol * width)
    width = width - 1
