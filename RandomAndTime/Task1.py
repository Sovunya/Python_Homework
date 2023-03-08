"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""

from time import *
def timer():
    start = time()
    total = 0
    while total < 1800:
        new = input()
        if new == 'off':
            end = time()
            total = round(end - start, 2)
            break
        end = time()
        total = round(end - start, 2)
        print(total)
    print(total)

timer()