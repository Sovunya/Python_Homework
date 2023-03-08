"""
Напишите скрипт который принимает 2 аргумента и записывает первый аргумент в файл где имя файла второй аргумент.
"""

import sys

if len(sys.argv) < 3:
    print("Необходимо передать 2 аргумента: содержимое файла и имя файла")
else:
    content = sys.argv[1]
    filename = sys.argv[2]
    with open(filename, "w") as file:
        file.write(content)
    print(f"Содержимое '{content}' успешно записано в файл '{filename}'")
