"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см *
число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _wieght = 0.025  # масса асфальта в тоннах для укладки 1 кв.м полотна дороги толщиной 1 см

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print(f'Создан новый объект класса Road длинной {self._length} метров и шириной {self._width} метров')

    def get_weight(self, thickness):
        """
        Метод для расчёта массы асфальта, которая потребуется для покрытия дороги
        :param thickness: толщина асфальтгого покрытия в см
        :return: результат вычислений
        """
        asp_weight_val = int(self._length * self._width * self._wieght * thickness)
        return f'Масса асфальта, который потребуется для укладки полотна дороги толщиной {thickness} см,' \
               f'равна {asp_weight_val} т\n'

# Создаем экземпляры и проверяем работу метода
r1 = Road(5000, 20)
w1 = r1.get_weight(5)
print(w1)

r2 = Road(2000, 10)
w2 = r2.get_weight(1)
print(w2)

r3 = Road(1000, 5)
w3 = r3.get_weight(5)
print(w3)
