class Hero:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper", 100, 10, 14)
hero2 = Hero("sniper", 200, 20, 24)
hero3 = Hero("sniper", 300, 30, 34)
hero4 = Hero("sniper", 400, 40, 44)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)