"""
Отчисляем студентов в 2 раза быстрее.
Создайте 2 функции для работы с очередью.
В первой функции запросите пользователя вводить фамилии или off для завершения,добавьте фамилию в очередь.
Во второй функции выводится сообщение что студент из очереди отчислен с фамилией студента.
В основном потоке добавьте в очередь пару фамилий и запустите функции в разных потоках.
"""

import queue
import threading

def add_student(queue):
    while True:
        name = input("Введите фамилию студента или 'off' для завершения: ")
        if name == 'off':
            break
        queue.put(name)

def remove_student(queue):
    while True:
        if queue.empty():
            continue
        name = queue.get()
        print(f"Студент {name} отчислен")

queue = queue.Queue()
add_thread = threading.Thread(target=add_student, args=(queue,))
remove_thread = threading.Thread(target=remove_student, args=(queue,))

add_thread.start()
remove_thread.start()

add_thread.join()
remove_thread.join()




