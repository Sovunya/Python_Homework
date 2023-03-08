"""
Напишите 2 функции
Первая должна принимать ширину, длинну и высоты комнаты и записывать в файл площадь комнаты из 4 стен.
Вторая должна записать в тот же файл расход краски исходя из соотношения 5л/кв.м.
"""

from multiprocessing import Process

def room(w, l, h):
    "Функция для площади стен"
    area = 2 * h * (w + l)
    print(f"Площадь стен: {area}")
    with open('room_info.txt', 'w') as f:
        f.write(str(area))


def calc(w, l, h):
    "Функция на расход краски"
    with open("room_info.txt","r")as f:
        f.seek(0)
        area = f.read()
    paint = 5 * float(area)
    with open('room_info.txt', 'a') as f:
        f.write(f' Расход краски: {paint} л.\n')

if __name__ == "__main__":
    width = float(input("Введите ширину комнаты: "))
    length = float(input("Введите длину комнаты: "))
    height = float(input("Введите высоту комнаты: "))

    p1 = Process(target=room, args=(width, length, height))
    p2 = Process(target=calc, args=(width, length, height))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
