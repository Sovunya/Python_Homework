"""
Напишите скрипт который в качестве параметра из командной строки принимает имя файла. Читает команды в этом файле и выполняет их
Протестируйте скрипт на файле comands.txt
"""

import sys

if len(sys.argv) < 2:
    print("Необходимо передать имя файла с командами в качестве аргумента")
else:
    filename = sys.argv[1]
    with open(filename, "r") as f:
        for line in f:
            command = line.strip()
            print(f"Выполняем команду: {command}")
            # здесь можно выполнить команду с помощью subprocess или os.system
