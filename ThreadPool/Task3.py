"""
Создайте функцию которая из файла Names.txt берет имена, превращает его в путь до файла и помещает в очередь.
Создайте функцию которая создает txt файл  по пути из очереди.
Запустите все в разных потоках.
"""

import os
import threading
from queue import Queue

def get_file_paths(queue):
    with open("Names.txt", "r") as file:
        names = file.read().splitlines()
        for name in names:
            file_path = os.path.join("files", name + ".txt")
            queue.put(file_path)

def write_file(queue):
    while not queue.empty():
        file_path = queue.get()
        with open(file_path, "w") as file:
            file.write("Hello, {}!".format(os.path.basename(file_path)))
        print("Записан файл:", file_path)

if __name__ == "__main__":
    file_queue = Queue()
    get_file_paths_thread = threading.Thread(target=get_file_paths, args=(file_queue,))
    get_file_paths_thread.start()

    write_file_threads = []
    for i in range(5):
        thread = threading.Thread(target=write_file, args=(file_queue,))
        thread.start()
        write_file_threads.append(thread)

    get_file_paths_thread.join()

    for thread in write_file_threads:
        thread.join()

    print("Готово!")

#Выдает непонятные ошибки. Подойду на паре уточнить по этому заданию