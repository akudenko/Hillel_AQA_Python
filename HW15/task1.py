# Есть фрагмент текста, состоящий из предложений.
# Предложение - это строка, которая начинается с большой буквы и заканчивается точкой,
# вопросительным или восклицательным знаком (или несколькими такими знаками).
# Слова состоят только из латинских букв, разделяются отделяются пробелами или запятыми с пробелами.
# Предложение может состоять из одного слова.
# Составить предложение из первых слов предложений фрагмента.
# Только первое слово итогового предложения должно быть с большой буквы, остальные с маленькой.
# Предложение должно заканчиваться точкой.

# def generate_sentence(text: str) -> str:
# pass
#
# "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."
# -> "Hello and who or yes claro."
# "Hola..." -> Hola.

import re

text = "Hello, cocroach. And where it is? Who, can do it?! Or vice versa!? Yes, it's difficult... Claro.."


def generate_sentence(text: str) -> str:

    pattern = '(?:^|[.!?] )([A-Z][a-z]+)'
    lst_of_words = re.findall(pattern, text)
    string = ''

    for i, el in enumerate(lst_of_words):
        if i == 0:
            string += el + ' '
        else:
            string += el.lower() + ' '

    result = string.strip() + '.'

    return result


print(generate_sentence(text))
