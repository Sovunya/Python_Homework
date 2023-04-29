"""
Изучите API сервиса cataas.com: https://cataas.com/#/
Реализуйте функции которые сохраняют:
2 картинки случайных котиков
2 картинки в оригинальном размере
2 пиксельных картинки
PS: Картинки пишутся как обычный файл открытый на запись в бинарном режиме
"""

import requests

def getcat():
    for i in range(2):
        r = requests.get('https://cataas.com/cat/cute')
        with open(f"cat{i}.jpg", "wb") as f:
            f.write(r.content)

        o = requests.get('https://cataas.com/cat?type=or')
        with open(f"cat{i+8}.jpg", "wb") as f:
            f.write(o.content)

        p = requests.get('https://cataas.com/cat?filter=pixel')
        with open(f"cat{i+12}.jpg", "wb") as f:
            f.write(p.content)

        print(r,'\n', o, '\n', p, '\n')

getcat()
