"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class Duck:
    def hello(self):
        print("I'm a little duck")
    def voice(self):
        print('Honk-honk')
    def clothes(self):
        print("I'm wearing a beanie")

class Human:
    def hello(self):
        print("I'm a big-big human")
    def voice(self):
        print('Kurlik-kurlik-kurlik')
    def clothes(self):
        print("I'm wearing a coat")

duck1 = Duck()
human1 = Human()

for animals in (duck1,human1):
    animals.hello()
    animals.voice()
    animals.clothes()
