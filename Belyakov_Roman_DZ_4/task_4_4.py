"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates().
Убедиться, что ничего лишнего не происходит.

"""


import utils  # Импорт модуля

print(utils.currency_rates("USD"))  # Проверка работы модуля
print(utils.currency_rates("DKK"))
print(utils.currency_rates("cad"))
print(utils.currency_rates("INR"))
print(utils.currency_rates("noname"))
code_1 = input('Введите тикер валюты: ')
print(utils.currency_rates(code_1))
