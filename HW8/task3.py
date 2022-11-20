# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

def sum_range(start, end) -> int:
    final_sum = 0

    if start > end:
        temp_el = start
        start = end
        end = temp_el

    for i in range(start, end + 1):
        final_sum += i

    return final_sum


print(sum_range(2, 1))