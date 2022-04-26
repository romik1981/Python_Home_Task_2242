"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random


# Класс карта лотто для формирования карточек и вывода их на экран
class LottoCard:

     def __init__(self):

        self.card = [[random.randint(1, 90) for _ in range(5)] for i in range(3)]

        for i in self.card:
            i.sort()
        for _ in range(4):
            for i in self.card:
                i.insert(random.randrange(len(self.card)), '')

     def __str__(self):
         under_line = "-" * 35
         card_line = "\n".join(["\t".join(map(str, i)) for i in self.card])
         return f'{under_line}\n{card_line}\n{under_line}'


# Класс пользователь
class Player(LottoCard):

    def __str__(self):
        under_line = f'{"-" * 9} Ваша карточка {"-" * 11}'
        down_line = "-" * 35
        card_line = "\n".join(["\t".join(map(str, i)) for i in self.card])
        return f'{under_line}\n{card_line}\n{down_line}'

    def cross_num(self, keg):
        for _ in self.card:
            if keg in _:
                _.insert(_.index(keg), '-')
                _.remove(keg)
        return self


# Класс компьютер
class Computer(LottoCard):

    def __str__(self):
        under_line = f'{"-" * 7} Карточка компьютера {"-" * 7}'
        down_line = "-" * 35
        card_line = "\n".join(["\t".join(map(str, i)) for i in self.card])
        return f'{under_line}\n{card_line}\n{down_line}'

    def cross_num(self, keg):
        for _ in self.card:
            if keg in _:
                _.insert(_.index(keg), '-')
                _.remove(keg)
        return self


# Класс игра в нём описанны основные игровые действия и запуск игры
class Game(LottoCard):

    def __init__(self):
        print('=========== Игра Лотто ===========')

        self.kegs = [n for n in range(1, 91)]

    def get_keg(self):
        random.shuffle(self.kegs)
        self.keg = random.choice(self.kegs)
        self.kegs.remove(self.keg)
        return f'Выпал бочонок: {self.keg} (осталось {len(self.kegs)})'

    def play_round(self):
        """
        Игровой раунд
        :return:
        0 - Игра продолжается
        1 - Пользователь проиграл
        2 - Пользователь выиграл
        3 - Игра завершена
        """
        print(game.get_keg())
        print(p, com, sep='\n')
        user_answer = input('Зачеркнуть цифру? (y/n) \n Для завершения введите (q)')

        for _ in com.card:
            if self.keg in _:
                com.cross_num(self.keg)

        n = 0
        if user_answer == 'y':
            for _ in p.card:
                if self.keg in _:
                    p.cross_num(self.keg)
                    return 0
            for _ in p.card:
                if self.keg not in _:
                    n += 1
            if n == 3:
                return 1

        if user_answer == 'n':
            for _ in p.card:
                if self.keg in _:
                    return 1

        n = 0
        for row in com.card:
            for _ in row:
                if not str(_).isdigit():
                    n += 1
        if n == 27:
            return 1

        n = 0
        for row in p.card:
            for _ in row:
                if not str(_).isdigit():
                    n += 1
        if n == 27:
            return 2
        if user_answer == 'q':
            return  3

        return 0

# Программу можно использовать как модуль в других кодах
if __name__ == '__main__':
    p = Player()

    com = Computer()

    game = Game()

    while True:
        counter = game.play_round()
        if counter == 1:
            print('Пользователь проиграл!')
            break
        elif counter == 2:
            print('Пользователь выиграл!')
            break
        elif counter == 3:
            print('Игра остановлена!')
            break
