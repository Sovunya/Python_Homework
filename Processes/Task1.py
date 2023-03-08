"""
Напишите 2 функции, одна считает сумму четных чисел, вторая нечетных
Запустите функции в разных процессах со значениями от 1 до 1000000
"""

import multiprocessing

def sum_even_numbers(start, end):
    "Функция для подсчета суммы четных чисел"
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            total += i
    print("Сумма четных чисел:", total)

def sum_odd_numbers(start, end):
    "Функция для подсчета суммы нечетных чисел"
    total = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            total += i
    print("Сумма нечетных чисел:", total)

if __name__ == '__main__':

    even_process = multiprocessing.Process(target=sum_even_numbers, args=(1, 1000000))
    odd_process = multiprocessing.Process(target=sum_odd_numbers, args=(1, 1000000))

    even_process.start()
    odd_process.start()

    even_process.join()
    odd_process.join()
