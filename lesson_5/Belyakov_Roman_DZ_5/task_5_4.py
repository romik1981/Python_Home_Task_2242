"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
сделать оптимизацию кода по памяти, по скорости.

"""
from time import perf_counter
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
start = perf_counter()
result = [src[i] for i in range(1, len(src)) if src[i - 1] < src[i]]  # List Comprehensions создаёт список элементов,
# которые больше предыдущего.
finish = perf_counter() - start
print(result, finish, sys.getsizeof(result), sep=',')

start_1 = perf_counter()


def get_numbers(list_in: list) -> iter:
    """Функция возвращает генератор, отдающий только те элементы входного списка, которые больше предыдущего"""

    for i in range(len(list_in) - 1):
        if list_in[i] < list_in[i + 1]:
            yield list_in[i + 1]


print(*get_numbers(src), end=' ')
finish_1 = perf_counter() - start_1
print(finish_1, sys.getsizeof(get_numbers(src)), sep=',')  # List Comprehensions работает в быстрее,
# чем генератор через цикл for, но занимает больше места.
