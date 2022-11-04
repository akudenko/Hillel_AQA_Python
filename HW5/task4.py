# Задание 4:
# Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.

text = input('Enter a text here: ')
result = ''

for item in text:
    if not item.isdigit():
        result = result + item

print(result)