"""
Запустите фоновый процесс который следит за сроком подписки пользователя( для примера 10 секунд) если время подписки вышло выведите надпись "Ваша подписка закончилась."
и завершите работу программы. В основной программе сыграйте с пользователем в игру "угадай число".
"""

import multiprocessing
import random
import time


def subscription_checker():
    """Фоновый процесс, который следит за временем подписки"""
    print("Подписка активна.")
    time.sleep(5)
    print("Ваша подписка закончилась.")
    exit()


def guess_game():
    """Функция игры "угадай число" """
    print("Добро пожаловать в игру 'Угадай число'!")
    secret_number = random.randint(1, 11)
    while True:
        guess = input("Введите число от 1 до 10: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Вы ввели неверное значение. Попробуйте снова.")
            continue
        if guess == secret_number:
            print("Вы угадали!")
            break
        else:
            print("Вы не угадали. Попробуйте еще раз.")


if __name__ == '__main__':
    # запуск фонового процесса
    p = multiprocessing.Process(target=subscription_checker)
    p.start()

    # запуск игры "угадай число"
    guess_game()

    # остановка фонового процесса
    p.terminate()
