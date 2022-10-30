# Вывести треугольник #2 с шириной N с помощью цикла while

width = int(input('Enter a width of a triangle: \n'))
symbol = '*'
counter = 1

while counter <= width:
    print(symbol * counter)
    counter = counter + 1