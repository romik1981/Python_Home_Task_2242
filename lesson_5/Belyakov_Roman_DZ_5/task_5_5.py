"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# Первый вариант
def get_uniq_numbers(list_in: list) -> list:
    """
    Функция создает список элементов не имеющих повторений в порядке их следования в исходном списке.
    :param list_in: входной список
    :return: возвращает список элементов не имеющих повторений в порядке их следования в исходном списке
    """
    uniq_numbers_set = set()
    tmp = set()
    for num in list_in:
        if num not in tmp:
            uniq_numbers_set.add(num)
        else:
            uniq_numbers_set.discard(num)
        tmp.add(num)
    result_1 = [el for el in list_in if el in uniq_numbers_set]
    return result_1


print(get_uniq_numbers(src))

# Второй вариант
result_2 = [num for num in src if src.count(num) == 1]  # С List Comprehensions код короче.
print(result_2)

# Третий вариант
result_3 = []
for num in src:
    if src.count(num) == 1:
        result_3.append(num)  # С циклом for и списком тоже более короткая запись.
print(result_3)
