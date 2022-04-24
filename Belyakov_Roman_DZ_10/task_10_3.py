"""
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
количества ячеек этих двух клеток.
Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом
случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод
make_order() вернёт строку: *****\n*****\n*****.
"""

class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f'Размер клетки после сложения: {self.quantity + other.quantity}'

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return f'Размер клетки после уменьшения: {self.quantity - other.quantity}'
        else:
            return f'Клетка исчезла!'

    def __mul__(self, other):
        return f'Размер клетки после умножения: {self.quantity * other.quantity}'

    def __floordiv__(self, other):
        return f'Размер клетки после деления на другую клетку: {self.quantity // other.quantity}'

    def __truediv__(self, other):
        return f'Размер клетки после деления на другую клетку(с округлением)): {round(self.quantity / other.quantity)}'

    def make_order(self, row):
        result = ''
        for i in range(self.quantity // row):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return f'Клетка размером {self.quantity}, по {row} в ряд, выглядит так:\n{result}'

cell = Cell(17)
cell1 = Cell(6)
cell2 = Cell(21)
print(cell + cell1)
print(cell - cell1)
print((cell - cell2))
print(cell * cell1)
print(cell1 * cell2)
print(cell // cell1)
print(cell / cell1)
print(cell.__floordiv__(cell2))
print(cell.make_order(5))
print(cell1.make_order(3))
print((cell2.make_order(9)))
