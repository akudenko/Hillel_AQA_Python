# Задание 6:
# Запросить у пользователя число N
# Запросить у пользователя N целых чисел и записать их в список A
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort).
# Вывести эти числа.

N = int(input('Enter the first number here: '))

A = []
maxValue = None
minValue = None

for _ in range(N):
    number = int(input('Enter a number here: '))
    A.append(number)

for i in A:
    if maxValue is None or i > maxValue:
        maxValue = i
    if minValue is None or i < minValue:
        minValue = i

print(f'Max value is: {maxValue}')
print(f'Min value is: {minValue}')

