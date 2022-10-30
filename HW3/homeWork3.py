# Пользователь вводит два числа A и B,
# нужно вывести сумму всех четных чисел в диапазоне от A до B.

a = int(input('Enter a number A: '))
b = int(input('Enter a number B: '))

sum = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        sum = sum + i

print(f'Sum is {sum}')

