"""
2)* (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
  num_translate_adv("One")
"Один"
 num_translate_adv("two")
"два"

"""


def num_translate_adv(value: str):
    """переводит числительное с английского на русский """
    e_r_dictionary = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    value_low = value.lower()
    if ord(value_low[0]) == ord(value[0]) + 32:
        str_out = e_r_dictionary.get(value_low) #в этой переменной должен оказаться результат перевода
        print(str_out.title())
    else:
        str_out = e_r_dictionary.get(value_low)
        print(str_out)





num_translate_adv("One")
num_translate_adv("Eight")
num_translate_adv("eight")
num_translate_adv("three")
num_translate_adv("fifteen")
