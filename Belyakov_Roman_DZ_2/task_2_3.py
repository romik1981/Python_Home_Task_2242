"""
3. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!
*(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, чем может сначала показаться.


"""


def convert_list_in_str(list_in: list) -> str:
    i = 0
    while i < len(list_in):
        if list_in[i].isdigit() and int(list_in[i]) // 10 != 0:
            list_in[i] = '"' + list_in[i] + '"'
            i += 1
        elif list_in[i].isdigit():
            list_in[i] = '"0' + list_in[i] + '"'
            i += 1
        elif list_in[i][0] == '+':
            list_in[i] = '"+0' + list_in[i][1:] + '"'
            i += 1
        elif list_in[i][0] == '-':
            list_in[i] = '"+0' + list_in[i][1:] + '"'
            i += 1
        i += 1
    print('Новый список не создан получился преобразованный: ', my_list, end='\n\n\n')
    str_out = ' '.join(list_in)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(convert_list_in_str(my_list))
