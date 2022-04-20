"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    # Создаём класс Matrix и переопределяем методы: __init__(), __str__(), __add__().
    def __init__(self, matrix):
        self.matrix = matrix

    # Перезагрузку метода можно выполнить 3 способами.
    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f'{i:5}', end='')
            print()
        return ''
        #return '\n'.join(map(str, self.matrix))
        #return '\n'.join(['\t'.join(map(str, i)) for i in self.matrix])

    def __add__(self, other):

        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    return f'Матрицы невозможно сложить!'
                for i_1 in range(len(other.matrix[i])):
                    self.matrix[i][i_1] = self.matrix[i][i_1] + other.matrix[i][i_1]
        else:
            return f'Матрицы невозможно сложить!'
        return self
        # return ((self.matrix[i][i_1] + other.matrix[i][i_1] for i_1 in range(len(other.matrix[i])))
        # for i in range(len(self.matrix)))


# Создаем классы и  проверяем работу методов.
m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m1 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
m2 = Matrix([[10, 11], [13, 14], [16, 17]])
print('Создана матрица:\n', m, sep='')
print('Создана матрица:\n', m1, sep='')
print('Создана матрица:\n', m2, sep='')
print('Результат сложения матриц:\n', m + m1, sep='')
print('Результат сложения матриц:\n', m1 + m2, sep='')
