# Написать класс-миксин, наследуя который объект будет выводится в консоль в виде имени класса и словаря аттрибутов со значениями:
# ClassName: {
#     key: value
# }

# class AttributePrinterMixin:
#     pass
# Протектед и приватные аттрибуты должны выводить только свое имя (без знака подчеркивания для протектед и префикса "_<имя класса>__")
#
# Каждя строка с полем начинается с символа табуляции.
# Если класс наслудует другие классы, их аттрибуты тоже должны выводится по тем же правилам.
# Свойства обрабатывать не надо.
# Пример:
# class A(AttributePrinterMixin):
#     def __init__(self):
#         self.public_filed = 3
#         self._protected_field = 'q'
#         self.__private_field = [1, 2, 3]
#
# a = A()
# print(a)
# A: {
#    public_filed: 3
#    protected_field: q
#    private_field: [1, 2, 3]
# }

class AttributePrinterMixin:
    def __repr__(self):
        attributes = {}
        for i in self.__dir__():
            if not i.startswith('__'):
                attributes.setdefault(i, getattr(self, i))
        lst = ''
        for i in attributes:
            if i.startswith('_'):
                i_ = i[1:]
                lst += f'    {i_}: {attributes[i]}\n'
            elif '__' in i:
                i__ = i.split('__')
                lst += f'    {i__[1]}: {attributes[i]}\n'
            else:
                lst += f'    {i}: {attributes[i]}\n'
        return f'{self.__class__.__name__}: {{\n{lst}}}'


class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]


a = A()
print(a)
