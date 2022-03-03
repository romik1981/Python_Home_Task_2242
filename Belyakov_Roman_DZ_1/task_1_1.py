"""
1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
	Примеры:
duration = 53
53 сек
duration = 153
2 мин 33 сек
duration = 4153
1 час 9 мин 13 сек
duration = 400153
4 дн 15 час 9 мин 13 сек


Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки работы кода сразу для
нескольких значений продолжительности, будет ли тут полезен список?

"""


# Функция для вычисления интервалов времени

def convert_time(duration):
    if duration < 60:
        return f'{duration} сек'  # Выводим количество секунд
    elif duration >= 60 and duration < 3600:
        minutes = duration // 60  # Рассчитаем количество минут
        seconds = duration % 60  # Рассчитаем количество секунд
        return f'{minutes} мин {seconds} сек'
    elif duration >= 3600 and duration < 86400:
        hours = duration // 3600  # Рассчитаем количество часов
        minutes = (duration % 3600) // 60
        seconds = (duration % 3600) % 60
        return f'{hours} час {minutes} мин {seconds} сек'
    elif duration >= 86400:
        days = duration // 86400  # Рассчитаем количество дней
        hours = (duration % 86400) // 3600
        minutes = (duration % 3600) // 60
        seconds = (duration % 3600) % 60
        return f'{days} дн {hours} час {minutes} мин {seconds} сек'

# Функция обратного перевода интервала времени в секунды

def rev_check(result):
    if len(result) == 6:
        int_1 = int(result[:-4])  # Выводим количество секунд
        return f'{int_1} сек'
    elif len(result) == 12:
        int_2 = int(result[-6:-4]) + int(result[:-11]) * 60  # Рассчитаем количество минут и секунд
        return f'{int_2} сек'
    elif len(result) == 18:
        int_3 = int(result[-6:-4]) + int(result[-12:-10]) * 60 + int(result[:-17]) * 3600  #  Рассчитаем количество часов, минут и секунд
        return f'{int_3} сек'
    elif len(result) >= 24:
        int_4 = int(result[-6:-4]) + int(result[-13:-11]) * 60 + int(result[-19:-17]) * 3600 + int(result[:-22]) * 86400  #Рассчитаем количество дней, часов, минут и секунд
        return f'{int_4} сек'

print(convert_time(53))
print(convert_time(153))
print(convert_time(4153))
print(convert_time(400153), end='\n\n\n')
result_1 = convert_time(53)
result_2 = convert_time(153)
result_3 = convert_time(4153)
result_4 = convert_time(400153)

duration = int(input('Введите временной интервал в сек: '))
result = convert_time(duration)
print(convert_time(duration))
print(type(result))
print(rev_check(result), end='\n\n\n')


print(rev_check(result_1))
print(rev_check(result_2))
print(rev_check(result_3))
print(rev_check(result_4))
"""
При попытке написать цикл обратной проверки временного интервала столкнулся с проблемой распарсивания строки переменной 
result, так как она имеет тип <str>  и сложно отделить буквы от цифр, не применяя методов строк, которые мы не изучали!
Прошу при разборе ДЗ рассмотреть варианты обратной проверки?! Не очень понял зачем тут нужен список, может быть словарь
для записи интервала в секундах и переведеннного интервала?! Потратил очень много времени на эту задачу, решить хотел
именно применяя методы рассмотреннные на уроке!!!
"""
