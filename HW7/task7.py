# Задание 7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4

import collections

f = open('words.txt', 'r')
words = (f.read()).split()

counter = collections.Counter(words)
topFiveWords = counter.most_common(5)

for key, value in topFiveWords:
    print(f"'{key}' - {value} раз")