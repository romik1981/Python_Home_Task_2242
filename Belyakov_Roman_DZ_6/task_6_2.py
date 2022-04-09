"""
2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания.
Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""


def get_spam_addr(dict_in: dict) -> tuple:
    """Находит адрес пославший больше всего запросов и возвращает кортеж (адрес, число запросов)"""
    max_count_addr = 0
    spam_addr = ''
    for key, val in dict_in.items():
        if val > max_count_addr:
            spam_addr = key
            max_count_addr = val

    return spam_addr, max_count_addr  # вернёт кортеж значений (адрес, число запросов)


dict_remote_addr = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for str_ in fr:
        if not str_.split()[0] in dict_remote_addr:
            dict_remote_addr.setdefault(str_.split()[0], 1)  # Создаём позицию IP адрес: запро в dict_remote_addr
        else:
            dict_remote_addr[str_.split()[0]] += 1

print('IP aдрес спамера и число его запросов: ', get_spam_addr(dict_remote_addr))
