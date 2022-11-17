# Задание 4
# Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число

import random

random_numbers = [random.randint(1, 100) for _ in range(100)]
print(random_numbers)

f = open('random_numbers.txt', 'w')
for i in random_numbers:
    f.writelines([str(i), '\n'])

f.close()