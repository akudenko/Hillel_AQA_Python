# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента

numbers = [1, 2, 3]


def change(lst=None) -> list:
    if lst is None:
        lst = []
    temp_el = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp_el

    return lst


change(numbers)

print(numbers)
