"""
7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и
новое значение. При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию,
когда пользователь вводит номер записи, которой не существует.
"""

import sys

list_seek = [0]
with open('bakery.csv', 'a+', encoding='utf-8') as fa:
    fa.seek(0)
    line = fa.readline()
    while line:
        list_seek.append(fa.tell())  # Считываем положение курсора и записываем его в список
        line = fa.readline()
if len(sys.argv) == 1:
    print('Введите номер записи и значение продаж?!')
elif len(sys.argv) == 2:
    print('Введите значение продаж?!')
elif int(sys.argv[1]) >= len(list_seek):
    print('Нет такой записи!')
else:
    with open('bakery.csv', 'r+', encoding='utf-8') as fa:
        fa.seek(list_seek[int(sys.argv[1]) - 1])
        fa.writelines(f'{sys.argv[2]}\n')  # Редактируем строку по заданным параметрам (номер записи, значение продаж)
