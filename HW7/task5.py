# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

f = open('file_with_texts.txt', 'r')
data = f.read()

words = data.split()

for i in words:
    if i.isdigit():
        words.remove(i)

print(f'Words in text is: {len(words)}')
