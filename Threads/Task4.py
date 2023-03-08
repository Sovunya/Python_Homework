"""
Создайте функцию которая принимает путь до файла из папки files и меняет в нем "ids" на "id".
Запустите функцию для каждого файла в отдельном потоке.
Измерьте время выполнения программы.
"""

import os
import re
import time
import threading

def replace_ids(file_path):

    with open(file_path, 'r') as f:
        contents = f.read()

    contents = re.sub('ids', 'id', contents)

    with open(file_path, 'w') as f:
        f.write(contents)

files = os.listdir('files')

start_time = time.time()
threads = []
for file in files:
    file_path = os.path.join('files', file)
    thread = threading.Thread(target=replace_ids, args=(file_path,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Программа завершена за {end_time - start_time} секунд")
