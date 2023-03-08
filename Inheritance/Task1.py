"""
Добавьте на основании классов из презентации класс Magician который наследует Hero. Со своими методами hello и atack.
"""

class Hero():
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Герой -> ', self.name)
        print('Здоровье героя -> ', self.health)
        print('Броня героя -> ', self.armor)
        print('Сила героя -> ', self.power)
        print('Снаряженеи героя -> ', self.weapon)

    def strike(self, enemy):
        print(
            '-> ', self.name, ' бьет ', enemy.name, ' на ', self.power, '\n'
            '-> Здоровье атакующего ' + str(self.health) + '. Броня атакующего ' + str(self.armor) + '\n'
            '-> Здоровье противника ' + str(enemy.health) + '. Броня противника ' + str(enemy.armor) + '\n'
            )

    def battle(self, enemy):
        while self.health > 0 and enemy.health > 0:
            enemy.armor -= self.power
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            self.strike(enemy)
            self.armor -= enemy.power
            if self.armor < 0:
                self.health += self.armor
                self.armor = 0
            if self.health <= 0:
                print('Hero died')
                print('Здоровье self ',self.health)
                print('Здоровье enemy ', enemy.health)
                break
            elif enemy.health <= 0:
                print('Hero win')
                print('Здоровье self ', self.health)
                print('Здоровье enemy ', enemy.health)
                break
            elif enemy.health > 0:
                enemy.strike(self)

class Magician(Hero):
    def hello(self):
        print('В пространсстве появляется небольшой светящийся щар и начинает разрастаться')
        print('В один момент он превращается в портал и оттуда выходит маг')

    def attack(self, enemy):
        print('Маг заряжает свой посох плазмой и атакует')

class Archer(Hero):
    def hello(self):
        print('Из леса выпригивает лучница')

    def attack(self, enemy):
        print('Лучница заряжает лук стрелой и стреляет')

magician1 = Magician('Гарольт', 100, 0, 20,'Посох теней')
magician1.hello()
magician1.print_info()

print('')

archer1 = Archer('Кхали', 85, 10, 22, 'Лук из рога свирели')
archer1.hello()
archer1.print_info()

print('')

archer1.battle(magician1)

