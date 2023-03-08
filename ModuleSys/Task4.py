"""
Напишите скрипт который принимает 2 аргумента - путь и имя папки. И создаем папку по указанному пути.
"""

import os
import sys

if len(sys.argv) < 3:
    print("Необходимо передать 2 аргумента: путь и имя папки")
else:
    path = sys.argv[1]
    folder_name = sys.argv[2]
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path)
    print(f"Папка '{folder_name}' создана в папке '{path}'")
