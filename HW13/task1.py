# Написать функцию, которая принимает несколько итерируемых объектов,
# и возвращает список из кортежей составленных из элементов итерируемых объектов одного индекса.
# Функция также должна принимать параметры с дефолтными значения:
#
# full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
# default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
#
# seq1 = [1, 2, 3, 4, 5]
# seq2 = [9, 8, 7]
# custom_zip(seq1, seq2) -> [(1, 9), (2, 8), (3, 7)]
# custom_zip(seq1, seq2, full=True, default="Q") -> [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
#
# Встроенную функцию zip не используем.
# def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:

from typing import Iterable, List, Tuple


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    min_sequences = min(*sequences, key=len)
    max_sequences = max(*sequences, key=len)
    result_tuple = [[] for i in max_sequences]
    for i in range(len(sequences)):
        for k in range(len(result_tuple)):
            if k < len(sequences[i]):
                result_tuple[k].append(sequences[i][k])
            else:
                result_tuple[k].append(default)
    if full:
        return [tuple(i) for i in result_tuple]
    else:
        return [tuple(i) for i in result_tuple[:len(min_sequences)]]


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=True, default="Q"))