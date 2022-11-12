# Задание 7:
# Пользователь вводит текст нужно вывести количество чисел в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 1234 dolor 1 sit amet
# Количество чисел: 3

#text = input('Enter the your text here: ')

text = "Lorem 222 ipsum, 1234 dolor 1 sit amet"

for i in text:
    if i.isdigit()