""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""

import os

os.chdir(r"D:\target")
os.mkdir("task4")
with open(os.path.join("task4", "answer.txt"), "w") as f:
    f.write("я выполнил задание")