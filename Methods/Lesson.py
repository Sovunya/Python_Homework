
class A():
    def __init__(self):
        self.number = 2

    def __add__(self, other):
        return self.number+other.number

    def __str__(self):
        return 'я магический метод'

    def  __lt__(self,other):    #меньше
        return self.number<other.number

    def __gt__(self, other):    #больше
        return self.number>other.number

class B():
    def  __init__(self):
        self.number = 3
        self.othernumber = 5
        self.anothernumber = 7

a = A()
b = B()
print(a)    #str
print(a+b)  #Переопределение оператора #add
print(a<b)
print(a>b)
print(type(3))  #Узнать тип чего-нибудь