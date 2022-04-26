class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    def __init__(self):
        """ Базовый класс склад оргтехники"""

    def __str__(self):
        return f'Создан базовый класс Склад Оргтехники'

class OfficeEquipment(Warehouse, OwnError):
    def __init__(self, equipment, quantity):
        super(OfficeEquipment, self).__init__()
        self.equipment = equipment
        self.quantity = quantity
        self.param = {self.equipment: self.quantity}

    def __str__(self):
        return f'Создан класс оргтехника с параметрами {self.param}'

    def to_take(self, quantity):
        try:
            if quantity.isdigit():
                n = int(self.param.get(self.equipment)) - int(quantity)
                self.param[self.equipment] = str(n)
                return f'Количество {self.equipment} на складе после передачи {self.param}'
            elif not quantity.isdigit():
                raise OwnError('Вы ввели не число!')
            elif quantity == None:
                raise TypeError

        except TypeError:
            print('Вы не ввели значение')

        except AttributeError:
            print('Ведите значение строкой')

        except OwnError as err:
            print(err)

        else:
            return f'Вы не ввели значение!'

    def to_give(self, quantity):
        n = int(self.param.get(self.equipment)) + quantity
        self.param[self.equipment] = str(n)
        return f'Количество {self.equipment} на складе после получения {self.param}'

class Printer(OfficeEquipment):
    def __init__(self, equipment, quantity, color, efficiency, manufacturer):
        super().__init__(equipment, quantity)
        self.color = color
        self.efficiency = efficiency
        self.manufacturer = manufacturer
        self.param.setdefault('Цвет', self.color)
        self.param.setdefault('Производительность', self.efficiency)
        self.param.setdefault('Производитель', self.manufacturer)

    def __str__(self):
        return f'Создан класс принтер с параметрами {self.param}'

class Scanner(OfficeEquipment):
    def __init__(self, equipment, quantity, color, efficiency, manufacturer):
        super().__init__(equipment, quantity)
        self.color = color
        self.efficiency = efficiency
        self.manufacturer = manufacturer
        self.param.setdefault('Цвет', self.color)
        self.param.setdefault('Производительность', self.efficiency)
        self.param.setdefault('Производитель', self.manufacturer)

    def __str__(self):
        return f'Создан класс сканер с параметрами {self.param}'


class Copier(OfficeEquipment):
    def __init__(self, equipment, quantity, color, efficiency, manufacturer):
        super().__init__(equipment, quantity)
        self.color = color
        self.efficiency = efficiency
        self.manufacturer = manufacturer
        self.param.setdefault('Цвет', self.color)
        self.param.setdefault('Производительность', self.efficiency)
        self.param.setdefault('Производитель', self.manufacturer)

    def __str__(self):
        return f'Создан класс копир с параметрами {self.param}'



w = Warehouse()
print(w)

e = OfficeEquipment('Xerox-2205', '3')
print(e)

p = Printer('Xerox-2205', '3', 'белый', '120 с/мин', 'Xerox')
print(p)

s = Scanner('S-1105', '3', 'белый', '100 с/мин', 'Sumsung')
print(s)

c = Copier('P-2205', '3', 'белый', '150 с/мин', 'Philips')
print(c)

p1 = p.to_take('1')
print(p1)

g = p.to_give(3)
print(g)
s1 = s.to_give(7)
print(s1)

c1 = c.to_take('2')
print(c1)
