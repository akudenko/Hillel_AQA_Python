# Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.

a = int(input('Enter a number A: '))
b = int(input('Enter a number B: '))
c = int(input('Enter a number C: '))

max = 0

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
elif c > a and c > b:
    max = c