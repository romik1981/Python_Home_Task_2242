
#result = '13 сек'
#result = '2 мин 33 сек'
#result = '1 час 9 мин 13 сек'
#result = '4 дн 15 час 9 мин 13 сек'


n = 12345
n = str(n)
print(n)

sum = 0
for i in n:
    i = int(i)
    sum += i

print(sum)


def sum_list_3():
    dataset = []
    # my_list = []
    sum_my_list_1 = 0  # Вводим необходимые для вычисления списки и переменные
    for n in range(1, 1000, 2):
        n = n ** 3 + 17
        dataset.append(n)  # Создаём список кубов нечетных чисел плюс 17
    for n in dataset:
        n = str(n)
        sum = 0
        for i in n:
            i = int(i)
            sum += i
        n = int(n)
        if sum % 7 == 0:
            sum_my_list_1 += n

    return sum_my_list_1


print(sum_list_3())


  # for indx in dataset:
   #     sum_my_list_1 += indx  # Вычисляем сумму членов этого списка
   # return sum_my_list_1  # Верните значение полученной суммы
