"""
Создать базовый класс ОЛИМПИАДНЫЕ ЗАДАНИЯ (данные об участнике, количество тестовых примеров,
количество пройденных тестов).
Создать производные классы ЗАДАНИЯ «ВСЕ ИЛИ НИЧЕГО»
(задается максимальное количество баллов за задание (даются только когда все тесты пройдены)
и ЗАДАНИЯ «ЧЕМ БЫСТРЕЕ, ТЕМ ЛУЧШЕ» (задается время участника на решение,
лучшее время всех участников, максимальное количество баллов за задание,
процент снижения балла в минуту отставания от лучшего времени).
Для заданных примеров задач, которые решали участники,
упорядочить участников по росту набранных баллов и определить суммарное количество баллов,
набранных заданным участником олимпиады.
Для проверки использовать действия над списком,
в котором разместить объекты разных производных классов.
"""

class Olympiad_tasks:
    def __init__(self,info,num_tst,num_slvd):
        self.info = info
        self.num_tst = num_tst
        self.num_slvd = num_slvd

class All_or_nothing_tasks(Olympiad_tasks):
    def __init__(self,info,num_tst,num_slvd,max_ball):
        super().__init__(info,num_tst,num_slvd)
        self.max_ball = max_ball

class The_faster_the_better_tasks(Olympiad_tasks):
    def __init__(self,info,num_tst,num_slvd,time_slvd,best_time,max_ball,prcnt_rdctn):
        super().__init__(info,num_tst,num_slvd)
        self.time_slvd = time_slvd
        self.best_time = best_time
        self.max_ball = max_ball
        self.prcnt_rdctn = prcnt_rdctn

Student1 = Olympiad_tasks('Борис Бритва', 10, 8)
Student2 =
Student3 =
Student4 =
Student5 =