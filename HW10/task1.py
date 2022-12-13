# Написать декоратор call_times, который будет принимать в качестве параметра file_name,
# считать количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'
#
# Пример:
# @call_times('foo.txt')
# def foo():
#   pass
#
# @call_times('foo.txt')
# def boo():
#   pass
#
# @call_times('calls.txt')
# def doo():
#   pass
#
# foo()
# boo()
# foo()
# foo()
# boo()
# doo()


# Файл foo.txt:
# foo была вызвана 3 раза
# boo была вызвана 2 раза
# Файл calls.txt:
#
# doo была вызвана 1 раза
#################################################################################################################

def call_times(file_name):
    def decorator(func):
        def inner():
            inner.count += 1
            f_name = func.__name__

            with open(file_name, 'w') as f:
                f.write(f'{f_name} была вызвана {inner.count} раз(а).\n')
            return func()

        inner.count = 0
        return inner

    return decorator


@call_times('foo.txt')
def foo():
    pass


@call_times('boo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
