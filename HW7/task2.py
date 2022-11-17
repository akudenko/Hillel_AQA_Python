# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt

text = input('Type text here: ')

f = open('data.txt', 'w')
f.write(text)