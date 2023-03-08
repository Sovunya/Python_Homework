"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""

def print_temperature(temperature):
    for temp in temperature:
        print(f"сегодня {temp} градусов")

temperature = [8, 3, -1]
print_temperature(temperature)

