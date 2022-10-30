# Вывести треугольник #3 с шириной N с помощью цикла while

width = int(input('Enter a width of a triangle: \n'))
symbol = '*'
spaceSymbol = ' '
counter = 0

while width != 0:
    print((spaceSymbol * counter) + (symbol * width))
    width = width - 1
    counter = counter + 1