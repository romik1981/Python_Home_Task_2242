"""

4)* (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия»
и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего
задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
 thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "И": {
        "И": ["Илья Иванов"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?

"""


def thesaurus_adv(*args) -> dict:
    dict_out = {}  # результирующий словарь значений
    for name in args:
        if name[name.index(' ') + 1] in dict_out:
            if name[0] in dict_out[name[name.index(' ') + 1]] and not name in dict_out[name[name.index(' ') + 1]][
                name[0]]:
                dict_out[name[name.index(' ') + 1]][name[0]].append(name)
            else:
                dict_out[name[name.index(' ') + 1]].setdefault(name[0], [name])
        else:
            dict_out[name[name.index(' ') + 1]] = {name[0]: list(
                filter(lambda el: el[0] == name[0] and el[el.index(' ') + 1] == name[name.index(' ') + 1], args))}

    return dict_out


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Алика Семенова",
                    "Евгений Андреев", "Зинаида Игнатьева", "Ангелина Сердюкова"))

dict_out = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                         "Алика Семенова",
                         "Евгений Андреев", "Зинаида Игнатьева", "Ангелина Сердюкова")


def sort_dict_last_name(dict_in: dict) -> dict:  # Финкция сортировки ключей словоря по алфавиту(по фимилии)
    dict_out_keys_last_name = sorted(dict_in)
    dict_out_adv = {}
    for _ in dict_out_keys_last_name:
        for key, val in dict_out.items():
            if key == _:
                dict_out_adv[key] = val
            else:
                pass
    return dict_out_adv


print('\n')
print(f' Словарь отсортированный по алфавиту(по фамилии):  {sort_dict_last_name(dict_out)}')

print('\n')


def sort_dict_first_name(dict_in: dict) -> dict:  # Финкция сортировки ключей словоря по алфавиту(по имени)
    """
    Функция сортировки словаря по имени
    :param dict_in: Принимает на вход словарь
    :return: Возвращает сортированный по имени словарь
    """
    dict_out_adv_1 = {}
    for key, val in dict_in.items():
        keys = sorted(dict_in[key])
        dict_out_adv_1.setdefault(key, {})
        for _ in keys:
            for key_1, val in dict_in[key].items():
                if key_1 == _:
                    dict_out_adv_1[key].setdefault(key_1, val)
            else:
                pass
    return dict_out_adv_1


print(f' Словарь отсортированный по алфавиту(по имени):  {sort_dict_first_name(sort_dict_last_name(dict_out))}')
