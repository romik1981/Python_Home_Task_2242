import sys

list_sale = []
with open('bakery.csv', 'r', encoding='utf-8') as fr:
    for str_ in fr:
        list_sale.append(str_.strip())

num_sale = sys.argv

if len(num_sale) == 1:
    for i, num in enumerate(list_sale, start=1):
        print(i, num)
elif len(num_sale) == 2:
    for i, num in enumerate(list_sale[int(sys.argv[1]) - 1:], start=int(sys.argv[1])):
        print(i, num)
elif len(num_sale) == 3:
    for i, num in enumerate(list_sale[int(sys.argv[1]) - 1:int(sys.argv[2])], start=int(sys.argv[1])):
        print(i, num)
