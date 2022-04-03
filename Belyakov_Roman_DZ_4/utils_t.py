import requests
import sys
import datetime


def currency_rates():
    """
    возвращает курс валюты `code` по отношению к рублю
    code: Тикер валюты
    :return: Возвращает строку с курсом валюты в рублях
    """
    code = list(map(str, sys.argv[1:]))
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_dict = {}
    currency_list = response.text.split('ID=')
    date = currency_list.pop(0)
    date = date[date.find('<ValCurs') + 15:date.find('name="Foreign Currency Market"><Valute ') - 2].split('.')
    date = datetime.date(year=int(date[2]), month=int(date[1]), day=int(date[0]))  # Приводим к классу "datetime.date"
    for _ in code:
        for element in currency_list:
            exchange_rate = element[(element.find('<Value>') + 7):element.find('</Value>')]
            exchange_rate = float(exchange_rate.replace(',', '.'))
            amendment = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
            currency_dict[
                (element[(element.find('<CharCode>') + 10):element.find('</CharCode>')])] = exchange_rate / amendment
        if _.upper() in currency_dict:
            result_value = f'На {date}курс валюты {_.upper()} = {currency_dict.get(_.upper()):.2f} руб.'
            # здесь должно оказаться результирующее значение str
        else:
            result_value = None  # Если валюты нет в словаре возвращает None
        print(result_value)
    return


if __name__ == '__main__':
    currency_rates()
