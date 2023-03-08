"""
Создайте функцию напоминалку в отдельном потоке от основном программы.
Функция должна запрашивать о чем напомнить и через сколько секунд.
В основной части программы запустите поток с функцией и выполните задержку в 10 секунд.
После выполнения программа должна написать "программа завершается"
"""

import time
from threading import Thread

def reminder():
    rem = input('Напомнить:\n')
    second = int(input('Через сколько секунд:\n'))
    time.sleep(second)

    print(rem)


th = Thread(target=reminder)
th.start()
time.sleep(10)
print('Программа завершается')

#th = Thread(target=reminder, daemon=True) #программа завершиться в любом случае
#th.start()
#time.sleep(10)
#th.join()  #ждет пока выполнится поток
#print('Программа завершается')