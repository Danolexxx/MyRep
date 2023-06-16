
class GameCharacter:
    def __init__(self, name, level, health, attack, protection):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.protection = protection
        self.health = self.health

    def hit(self):
        return self.attack or 5

    def damage(self,dam):
        damage = dam - (self.protection * 10 / 100)
        self.health -= damage
        if self.health <= 0:
            print(f'{self.name} убит')
            return True
        else:
            print(f'{self.name} получил урон {damage}, осталось здоровья {self.health}')
            return False

    def healing(self):
        self.health=100

    def level_up(self):
        self.level += 1
        self.health += round((self.health * 10) / 100)
        self.attack += round((self.attack * 10) / 100)
        print(f'Уровень {self.name} {self.level}. Здоровье {self.health},'
              f' атака {self.attack}')


GameCharacter1 = GameCharacter('Ваня', 1, 100, 10, 10)
GameCharacter2 = GameCharacter('Петя', 1, 100, 10, 10)

count1 = 0
count2 = 0
for i in range(3):
    boolean = True
    while boolean:
        if GameCharacter1.damage(GameCharacter2.hit()):
            print(f'Раунд {i+1}. Победитель {GameCharacter2.name}')
            GameCharacter2.level_up()
            count2 += 1
            boolean = False
        elif GameCharacter2.damage(GameCharacter1.hit()):
            print(f'Раунд {i+1}. Победитель {GameCharacter1.name}')
            GameCharacter1.level_up()
            count1 += 1
            boolean = False
    GameCharacter1.healing()
    GameCharacter2.healing()

if count1 > count2:
    print(f'Победил {GameCharacter1.name}')
else:
    print(f'Победил {GameCharacter2.name}')