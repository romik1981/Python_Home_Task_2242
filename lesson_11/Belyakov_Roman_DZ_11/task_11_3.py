class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = input('Введите числа для делимое: ')
b = input('Введите числа для делитель: ')
try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise OwnError('На ноль делить нельзя!')

except ValueError:
    print('Вы не ввели числа')

except OwnError as err:
    print(err)

else:
    print(f'Всё хорошо! Результат деления: {a / b}')

