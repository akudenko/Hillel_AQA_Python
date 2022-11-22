# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).


def read_last(lines, file):
    if isinstance(lines, float) or lines <= 0:
        return print(f'Wrong lines value: "{lines}" but should be int and more than 0')
    else:
        f = open(file, 'r')

        last_strings = f.readlines()[-lines:]
        f.close()

        for line in last_strings:
            print(line)


read_last(2, 'text.txt')