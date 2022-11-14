# Задание 7:
# Пользователь вводит текст нужно вывести количество чисел в этом тексте
# Пример:
# > 'Lorem 222 ipsum, 1234 dolor 1 sit amet
# Количество чисел: 3

text = input('Enter the your text here: ')
i = 0
digitIndex = 0
numberList = []
numbers = ''

while i <= len(text) - 1:
    if text[i].isdigit():
        numbers += text[i]
        if not text[i + 1].isdigit():
            i += 1
            numberList.append(numbers)
            numbers = ' '
            continue
    i += 1

print(f'Количество чисел: {len(numberList)}')


