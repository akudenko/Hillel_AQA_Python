#1.Пользователь вводит с клавиатуры три числа в переменные a, b, c.
#Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no

a = int(input('Enter a number A: '))
b = int(input('Enter a number B: '))
c = int(input('Enter a number C: '))

if (a > 10 and b > 10 and c > 10) and (a % 3 == 0) and (b % 3 == 0):
    print('yes')
else:
    print('no')