# 1. Написать функцию, которая возвращает слуайную строку заданной длины.
#
# Строка должна состоять из больших и маленьких латинских букв и цифр.
#
# def get_random_string(length: int) -> str:
#   pass
#
# Ограничения:
# - Не использовать модуль string
# - Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]
#################################################################################################################
from random import randint, choice


def get_random_string(length: int) -> str:
    list_of_chars = []
    string = ''

    for i in range(length):
        list_of_chars.append(chr(randint(65, 90)))
        list_of_chars.append(chr(randint(97, 122)))
        list_of_chars.append(chr(randint(48, 57)))
        char = choice(list_of_chars)
        string += char

    return string


print(get_random_string(7))
