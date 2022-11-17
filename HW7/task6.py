# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

f = open('numbers_separeted_by_spaces.txt', 'r')
data = f.read()

numbers = data.split()
summa = 0

for i in numbers:
    summa += int(i)

print(f'Sum is: {summa}')