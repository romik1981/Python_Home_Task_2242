"""
2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) и
возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

"""
import requests


def currency_rates(code: str) -> str:
    """
    возвращает курс валюты `code` по отношению к рублю
    :param code: Тикер валюты
    :return: Возвращает строку с курсом валюты в рублях
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_dict = {}
    currency_list = response.text.split('ID=')
    del currency_list[0]
    for element in currency_list:
        exchange_rate = element[(element.find('<Value>') + 7):element.find('</Value>')]
        exchange_rate = float(exchange_rate.replace(',', '.'))
        amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
        currency_dict[
            (element[(element.find('<CharCode>') + 10):element.find('</CharCode>')])] = exchange_rate / amendment
    if code.upper() in currency_dict:
        result_value = f'Курс валюты {code.upper()} = {currency_dict.get(code.upper()):.2f} руб.'  # здесь должно оказаться результирующее значение str
    else:
        result_value = None  # Если валюты нет в словаре возвращает None
    return result_value


print(currency_rates("USD"))
print(currency_rates("AUD"))
print(currency_rates("eur"))
print(currency_rates("BYN"))
print(currency_rates("noname"))
code = input('Введите тикер валюты: ')
print(currency_rates(code))
