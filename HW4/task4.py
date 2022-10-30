# Вывести треугольник #4 с шириной N с помощью цикла while

width = int(input('Enter a width of a triangle: \n'))
symbol = '*'
spaceSymbol = ' '
counter = 1
minValue = 1

while minValue <= width:
    widthOfSpaces = width - 1
    print((spaceSymbol * widthOfSpaces) + (symbol * counter))
    width = width - 1
    counter = counter + 1