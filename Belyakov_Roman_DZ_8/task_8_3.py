"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
 a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:
 a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

from functools import wraps


def type_logger(verbosity=0):
    """ Функция декоратор выводит название функции и аргумент(тип) или (значение, тип) """
    cache = {}
    def loger(func):
        @wraps(func)  # маскирование работы декоратора
        def wrapper_cache(name):
            if verbosity == 0:
                if name not in cache:
                    cache[name] = func(name), type(func(name))  # значение функции и её тип
            elif verbosity > 0:
                if name not in cache:
                    cache[name] = type(func(name))
            return cache
        return wrapper_cache

    return loger


@type_logger()  # запуск декоратора
#@type_logger(1)
def calc_cube(x):
    """func to calculate x ** 3"""
    return x ** 3


a = calc_cube(5)
a1 = calc_cube(10)
a2 = calc_cube(3.1)
print(calc_cube.__doc__)
print(calc_cube.__name__, a)  # вывод названия функции, её значения, аргументы, тип
