# Написать функцию которая принимает целое число - number.
# Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'.
# Запрещено пользоваться функцией или оператором возведение в степень.
#
# Пример:
#
# is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
#
# is_power_of_two(125) # 'no' потому что это не степень двойки

def is_power_of_two(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    elif 1 < number < 2:
        return 0
    else:
        return is_power_of_two(number / 2)


if is_power_of_two(256) == 1:
    print('yes')
else:
    print('no')
