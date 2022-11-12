# Задание 5:
# Запросить у пользователя 5 чисел и записать их в список A
# Записать все числа из списка A которые больше 5 в список C

A = []
C = []

for _ in range(5):
    number = int(input('Enter a number here: '))
    A.append(number)
    if number > 5:
        C.append(number)
