"""
2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
ключевое слово yield.
"""

n = 15

odd_nums = (num for num in range(1, n + 1, 2))  # Генератор возвращающий нечётные числа от 1 до n (включительно)

print(*odd_nums, sep='\n')
#print(next(odd_nums))  # Когда числа в генераторе закончатся ...StopIteration
