"""
5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта
"""


import  sys


def prepare_dataset_u(path_users_file: str) -> list:
    """
   Считывает данные из файлов и возвращает список ФИО (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Возвращает списк пользователей
    """
    users_list = []
    with open(path_users_file, 'r', encoding='utf-8') as fr:
        line = fr.readline()
        while line:
            users_list.append(line.replace(',', ' ').strip())  # Список пользователей.
            line = fr.readline()

    return users_list

def prepare_dataset_h(path_hobby_file: str) -> list:
    """
      Считывает данные из файлов и возвращает список данных о хобби (список строковых переменных)
       :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
       :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
       :return: Возвращает списк хобби
       """
    hobby_list = []
    with open(path_hobby_file, 'r', encoding='utf-8') as fr:
        line = fr.readline()
        while line:
            hobby_list.append(line.replace(',', '').strip())  # Список хобби.
            line = fr.readline()
    if len(prepare_dataset_u('users.csv')) >= len(hobby_list):
        while len(prepare_dataset_u('users.csv')) > len(hobby_list):
            hobby_list.append(None)
    else:
        hobby_list = sys.exit(1)

    return hobby_list

users = str(sys.argv[1])
hobby = str(sys.argv[2])
users_hobby = str(sys.argv[3])

with open(users_hobby, 'w', encoding='utf-8') as fw:
    for user, hobby in zip(prepare_dataset_u(users), prepare_dataset_h(hobby)):
        fw.writelines(f'{user}: {hobby}\n')  # Записывает в файл пару ФИО: хобби.
