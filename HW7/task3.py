# Задание 3
# Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел

number = int(input('Type a first number here: '))
numbers = []

for i in range(number):
    numbers.append(int(input('Type number here: ')))
    i += 1

f = open('numbers.txt', 'w')
f.writelines(str(number))
f.writelines(' ')
f.writelines(str(numbers))
