"""
Создайте функцию которая выводит на экран все делители числа.
Создайте очередь и добавьте в нее числа.
Создайте пул потоков и запустите в пуле функцию с очередью.
"""

import queue
import threading


def find_divisors(q):
    while not q.empty():
        num = q.get()
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        print(f"Делители числа {num}: {divisors} \n")


def main():
    nums = [12, 23, 36, 49, 60]
    q = queue.Queue()
    for num in nums:
        q.put(num)

    num_threads = 3
    pool = []
    for i in range(num_threads):
        t = threading.Thread(target=find_divisors, args=(q,))
        t.start()
        pool.append(t)

    for t in pool:
        t.join()


if __name__ == "__main__":
    main()
