"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например
{"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров.
"""


class Worker:
    # Создаём конструктор класса и определяем атрибуты класса
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}
        print(f'Создан класс Worker для {surname} {name} - {position}')

class Position(Worker):
    # Создаём методы класса
    def get_full_name(self):
        return f'Полное имя: {self.surname} {self.name}'

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        return f'Доход: {total_income} руб\n'

# Создаём экземпляры классов и проверяем работу методов
w1 = Position('Иван', 'Иванов', 'инженер', 1000, 500)
print(w1.get_full_name())
print(w1.get_total_income())

w1 = Position('Пётр', 'Сидоров', 'электромонтёр', 1200, 250)
print(w1.get_full_name())
print(w1.get_total_income())

w1 = Position('Анна', 'Чехова', 'бухгалтер', 5000, 700)
print(w1.get_full_name())
print(w1.get_total_income())
