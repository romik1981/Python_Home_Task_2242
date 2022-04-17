"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    # Создаём конструктор класса и определяем атрибуты класса
    def __init__(self, name, color, max_speed, is_police):
        self.name = name
        self.color = color
        self.max_speed = max_speed
        self._is_police = is_police
        print(f'Создан класс Car для автомобиля {name}: цвет - {color}, максимальная скорость - {max_speed} км/ч')

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}!')

    def show_speed(self, speed):
        self.speed = speed
        print(f'{self.name} движется со скоростью {speed} км/ч')


class TownCar(Car):
    # Создаём дочерний класс(городской автомобиль), переопределяем атрибут скорость
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это городской автомобиль.')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)
        if self.speed > 60 and not self._is_police:
            print('Ваш автомобиль превышает допустимую скорость движения!!!')  # Выводим сообщение о превышении скорости


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это спортивный автомобиль.')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это грузовой автомобиль.')

    def show_speed(self, speed):
        self.speed = speed
        super().show_speed(self.speed)
        if self.speed > 40 and not self._is_police:
            print('Ваш автомобиль превышает допустимую скорость движения!!!')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это полицейский автомобиль.')


# Создаем экземпляры автомобилей и проверяем работу методов
auto1 = TownCar('Audi-80', 'красный', 220, False)
auto1.go()
auto1.turn('направо')
auto1.show_speed(35)
auto1.show_speed(55)
auto1.show_speed(75)
auto1.stop()
print()
auto2 = SportCar('BMW-X6', 'серый', 270, False)
auto2.go()
auto2.turn('налево')
auto2.show_speed(155)
auto2.stop()
print()
auto3 = WorkCar('МАЗ-5440', 'бежевый', 90, False)
auto3.go()
auto3.turn('налево')
auto3.turn('направо')
auto3.show_speed(35)
auto3.stop()
print()
auto4 = PoliceCar('Lada-2120', 'бело-синий', 170, True)
auto4.go()
auto4.turn('направо')
auto4.show_speed(95)
auto4.stop()
