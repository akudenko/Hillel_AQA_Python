# Задание 3:
# Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

text = input('Enter a text here: ')
subStr = 'abc'

if text.find(subStr) != -1:
    text = text.replace(subStr, 'www')
else:
    text = text + 'zzz'