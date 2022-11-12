# Задание 4:
# Запросить у пользователя число N
# Запросить у пользователя N чисел и записать их в список A
# Вывести список в обратной последовательности

N = int(input('Enter the first number here: '))

A = []

for _ in range(N):
    number = int(input('Enter a number here: '))
    A.append(number)

A.reverse()
print(A)