# Задание 2:
# Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

text = input('Enter a text here: ')
word = input('Enter a word that should be found: ')

if text.find(word) != -1:
    print('YES')
else:
    print('NO')