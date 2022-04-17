"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""

import time


class TrafficLight:
    # определяем цвета светофора
    red_color = 'красный'
    yellow_color = 'жёлтый'
    green_color = 'зелёный'

    # определяем время работы цветов светофора
    red_color_wait = 7
    yellow_color_wait = 2
    green_color_wait = 5

    def __init__(self, color):
        """ Конструктор класса TrafficLight"""
        self.__color = color  # аттрибут color(цвет)
        print(f'Создан новый объект TrafficLight с базовым цветом {self.__color}')

    def switch_light(self, color, wait_period):
        """ Метод переключения цветов светофора"""
        self.wait_period = wait_period
        print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
        time.sleep(self.wait_period)

    def running(self, color='', k=1):
        """
        Метод запуска светофора
        :param color: цвет старта светофора
        :param k: число циклов работы светофора
        """
        n = 0
        while n != k:
            if not color:
                loc_color = self.__color
            else:
                loc_color = color

            if loc_color == self.red_color:
                self.switch_light('красный', self.red_color_wait)
                self.switch_light('желтый', self.yellow_color_wait)
                self.switch_light('зеленый', self.green_color_wait)
            elif loc_color == self.yellow_color:
                self.switch_light('желтый', self.yellow_color_wait)
                self.switch_light('зеленый', self.green_color_wait)
            elif loc_color == self.green_color:
                self.switch_light('зеленый', self.green_color_wait)
            color = self.red_color
            n += 1

        print('\nЦикл работы светофора завершен')


# Инициализируем класс TrafficLight с базовым цветом и проверяем работу метода
traffic_light = TrafficLight('зелёный')
traffic_light.running()

traffic_light = TrafficLight('красный')
traffic_light.running()

traffic_light = TrafficLight('жёлтый')
traffic_light.running()

# Инициализируем класс TrafficLight с базовым цветом и проверяем работу метода изменив цвет включения на жёлтый
traffic_light = TrafficLight('красный')
traffic_light.running('жёлтый')

# Инициализируем класс TrafficLight с базовым цветом и проверяем работу метода изменив цвет включения на жёлтый,
# число циклов работы светофора 3
traffic_light = TrafficLight('красный')
traffic_light.running('жёлтый', k=3)
