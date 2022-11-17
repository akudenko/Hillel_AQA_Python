# Задание 1
# Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

f = open('text1.txt', 'r')
numbers = []
data = f.read()
f.close()

for i in data:
    if i.isdigit():
        numbers.append(i)

print(numbers)