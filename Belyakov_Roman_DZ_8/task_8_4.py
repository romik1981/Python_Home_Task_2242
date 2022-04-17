"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
...
@val_checker(lambda x: x > 0)
def calc_cube(x):
return x ** 3
 a = calc_cube(5)
125
 a = calc_cube(-5)
Traceback (most recent call last):
...
raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""

from functools import wraps

def val_checker(func_filter):

    def checker(func):

        @wraps(func)
        def decorator(x):
            if func_filter(x):
                return func(x)

            msg = f'wrong val {x}'
            raise ValueError(msg)
        return decorator

    return checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """func to calculate x ** 3"""
    return x ** 3

print(calc_cube.__doc__)

a = calc_cube(5)
print(a)
a1 = calc_cube(10)
print(a1)
a2 = calc_cube(-5)
print(a2)
