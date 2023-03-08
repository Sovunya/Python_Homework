"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""

from random import randint

startstop = input('1 - Подбросить кубы, 0 - Остановить:')
while startstop != '0':
    if startstop == '1':
        dice_1 = randint(1, 6)
        dice_2 = randint(1, 6)
        print(dice_1, dice_2)
        startstop = input('1 - Подбросить кубы, 0 - Остановить:')
    else:
        print('Нет накой команды')
        startstop = input('1 - Подбросить кубы, 0 - Остановить:')