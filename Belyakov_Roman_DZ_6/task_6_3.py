"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой между строками
    :return: Dict(str: Union[List[str]|None])
    """

    with open(path_users_file, 'r', encoding='utf-8') as fr:
        users_list = fr.read().split()

    hobby_list = []
    with open(path_hobby_file, 'r', encoding='utf-8') as fr:
        for str_ in fr:
            hobby_list.append(str_.replace(',', '').strip())

    users_dict = {}
    if len(users_list) >= len(hobby_list):
        while len(users_list) > len(hobby_list):
            hobby_list.append(None)
        counter = 0
        for name in users_list:
            users_dict[name.replace(',', ' ')] = hobby_list[counter]
            counter += 1
    else:
        users_dict = sys.exit(1)

    return users_dict  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')  # файлы hobby1.csv и hobby2.csv нужны для проверки записи None
# и выхода с кодом 1
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=1, sort_keys=True)
