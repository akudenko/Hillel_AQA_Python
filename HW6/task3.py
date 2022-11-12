# Задание 3:
# Запросить у пользователя 10 чисел и записать их в список A
# Запросить у пользователя число N
# Вывести пользователю сколько в списке A повторяется число N

A = []

for _ in range(10):
    number = int(input('Enter a number here: '))
    A.append(number)

N = int(input('Enter the new number here: '))

print(f'Number {N} repeated {A.count(N)} times in a list A')