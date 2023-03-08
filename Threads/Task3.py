"""
Создайте функцию в демоне потока которая каждые 3 секунды будет писать "Вводите быстрее".
В основной части программы запросите ввод кода от бомбы и если код неверный выведите: "Вы взорвались", если верный - "Бомба разминирована"
"""

import threading
import time

def prompt():
    while True:
        print("Вводите быстрее")
        time.sleep(3)

prompt_thread = threading.Thread(target=prompt)
prompt_thread.daemon = True
prompt_thread.start()