class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num = []
while True:
    a = input('Введите числo (stop для выхода): ')
    try:
        if a == 'stop':
            print('Ваш список чисел: ', num)
            break
        elif a.isdigit():
            a = int(a)
            num.append(a)
        elif not a.isdigit():
            raise OwnError('Вы ввели не число!')

    except ValueError:
        print('Вы не ввели число')

    except OwnError as err:
        print(err)

    else:
        print(f'Всё хорошо! Ваш список чисел: {num}')
