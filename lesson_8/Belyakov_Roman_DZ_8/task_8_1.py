"""
1. Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
 email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
 email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
"""

import re

pattern = r"^(?P<key>[a-zA-Z0-9\_/-]+)@(?P<val>[a-z]+\.[a-z]+)$"  # шаблон регулярного выражения
def email_parse(email_address: str):
    """
    Функция извлекает имя пользователя почтовый домен из email адреса и возвращает в виде словаря
    :param email_address: адресс электронной почты
    :return: возвращает словарь {'username': 'пользователь', 'domain': 'доменный адрес'}
    """


    RE_E_MAIL = re.compile(pattern)

    if RE_E_MAIL.match(email_address) == None:  # Условие если адрес не валиден
        msg = f'wrong email {email_address}'
        raise ValueError(msg)

    else:
        print(*map(lambda x: x.groupdict(), RE_E_MAIL.finditer(email_address)), sep=',')

print(email_parse.__name__) # вывод названия функции
print(email_parse.__doc__)  # вывод её документирования


email_parse('some-123@geekbrains.ru')
email_parse('Someone@geekbrains.ru')
email_parse('Some_one/@geekbrains.com')
email_parse('someone.geekbrains.ru')
email_parse('retапр/o@gmail.com')
