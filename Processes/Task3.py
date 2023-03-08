"""
Напишите функцию которая через канал обмена возвращает количество валюты которую можно приобрести на n сумму денег при курсе 1 к 75.
Запустите функцию в отдельном процессе и отправьте в нее данные задержкой в 0.5 секунды передайте ей разное количество доступных денег.
Выводите количество валюты на экран по мере обработки данных.
"""

import time
import multiprocessing as mp

def get_currency(amount, conn):
    currency = amount // 75
    conn.send(currency)
    conn.close()

if __name__ == '__main__':
    amounts = [100, 200, 500, 1000]
    for amount in amounts:
        parent_conn, child_conn = mp.Pipe()
        p = mp.Process(target=get_currency, args=(amount, child_conn))
        p.start()
        time.sleep(0.5) # задержка в 0.5 секунды
        currency = parent_conn.recv()
        print(f'{amount} сум = {currency} валюты')
        p.join()
