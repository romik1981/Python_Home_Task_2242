import re

class Data:

    def __init__(self, date):
        self.date = date

    @classmethod
    def number(cls, data):
        return  int(data.replace('-', ''))

    @staticmethod
    def valid_data(date):
        RE_DATE = re.compile(r'^(\d{2}[./-]){2}\d{4}$')
        if RE_DATE.match(date):
            return f'valid date {date}'
        elif not RE_DATE.match(date):
            return f'wrong date {date}'

m = Data.number('22-12-2022')
print(m)
d = Data.valid_data('11-03-2019')
d1 = Data.valid_data('11,03,2019')
d1 = Data.valid_data('17.05.2022')
print(d, d1, sep='\n')