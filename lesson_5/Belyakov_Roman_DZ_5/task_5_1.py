"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
 odd_to_15 = odd_nums(15)
 next(odd_to_15)
1
 next(odd_to_15)
3
...
 next(odd_to_15)
 next(odd_to_15)
...StopIteration...
"""

n = 15


def odd_nums(n: int):
    """
    Генератор возвращающий нечётные числа от 1 до n (включительно)
    :param n: конечное число генератора
    :yield: сохраняет состояние генератора
    """
    for num in range(1, n + 1, 2):
        yield num


odd_to_15 = odd_nums(n)
for _ in range(1, n + 3, 2):
    print(next(odd_to_15))  # Когда числа в генераторе закончатся ...StopIteration
