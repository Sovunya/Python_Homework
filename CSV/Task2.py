"""
Из данных в файле Task1.csv сделайте словарь вида:
(Имя,фамилия):{оценка: звание}
"""

import csv

info ={}

with open('Task1.csv', "r", newline="") as file:
    reader = csv.reader(file,delimiter=";")
    for row in reader:
        info[(row[0],row[1])]= row[2],row[3]
print(info)