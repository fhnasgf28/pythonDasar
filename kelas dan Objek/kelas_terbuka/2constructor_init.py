class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper", 100, 10, 4)
hero2 = Hero("sniper", 200, 15, 40)
hero3 = Hero("sniper", 1000, 10, 4)

print(hero1.__dict__)
print(hero3.__dict__)
print(hero2.__dict__)