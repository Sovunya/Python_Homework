"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""

import csv

subjects = [
    ["Астрология", "Козлов В.А", 8],
    ["Программирование", "Чиж П.П", 9],
    ["Квантовая физика", "Кренделев К.Г", 7],
    ["Образовательная программа 'Учимся считать'", "Мячиков П.П", 6]
]

filename = "Ilin.csv"

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Препод", "Моя любовь к предмету"])
    writer.writerows(subjects)
