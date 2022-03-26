"""
3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
какой тип данных лучше использовать в ответе функции?
"""

import requests
import datetime


def currency_rates(code: str) -> str:
    """
    возвращает курс валюты `code` по отношению к рублю
    :param code: Тикер валюты
    :return: Возвращает строку с курсом валюты в рублях
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_dict = {}
    currency_list = response.text.split('ID=')
    date = currency_list.pop(0)
    date = date[date.find('<ValCurs') + 15:date.find('name="Foreign Currency Market"><Valute ') - 2].split('.')
    date = datetime.date(year=int(date[2]), month=int(date[1]), day=int(date[0]))  # Приводим к классу "datetime.date"
    for element in currency_list:
        exchange_rate = element[(element.find('<Value>') + 7):element.find('</Value>')]
        exchange_rate = float(exchange_rate.replace(',', '.'))
        amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
        currency_dict[
            (element[(element.find('<CharCode>') + 10):element.find('</CharCode>')])] = exchange_rate / amendment
    if code.upper() in currency_dict:
        result_value = f'На {date} курс валюты {code.upper()} = {currency_dict.get(code.upper()):.2f} руб.'
        # здесь должно оказаться результирующее значение str
    else:
        result_value = None  # Если валюты нет в словаре возвращает None
    return result_value


print(currency_rates("USD"))
print(currency_rates("AUD"))
print(currency_rates("eur"))
print(currency_rates("BYN"))
print(currency_rates("noname"))
code_1 = input('Введите тикер валюты: ')
print(currency_rates(code_1))
