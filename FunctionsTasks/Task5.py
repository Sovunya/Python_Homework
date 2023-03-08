"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""


def test():
    name = input('Имя студента:')
    while name != "стоп":
        ans = 0
        num_lesns = int(input('Число предметов:'))
        for i in range(num_lesns):
            lessn = int(input('Количество баллов:'))
            if lessn >= 0 and lessn <= 50:
                ans += lessn
                print('Итоговый счёт:', ans)
            else:
                print('Неправильное число')
        if ans > 80:
            print('Наградить дипломом.')
        elif ans > 50 and ans <= 80:
            print('Наградить похвальной грамотой.')
        else:
            print('Выдать грамоту об участии.')
        name = input('Имя студента:')


test()