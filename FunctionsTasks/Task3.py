"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""

def num_usr():
    pipl = int(input('Число учеников:'))
    for i in range(pipl):
        print(input('Имя ученика:'))
        ball = int(input('Балл:'))
        if ball >= 50:
            print('True')
        elif ball <= 50:
            print('Вы отчислены')
        else:
            return 0
num_usr()