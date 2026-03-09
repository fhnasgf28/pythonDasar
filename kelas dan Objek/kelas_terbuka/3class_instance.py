class Hero:
    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print('membuat hero dengan nama ' + inputName, inputHealth, inputPower)


hero1 = Hero("sniper", 1000, 10, 4)
print(Hero.jumlah)
hero2 = Hero("Mirana", 100, 15, 1)
print(Hero.jumlah)
hero3 = Hero("Ucup", 1000, 100, 20)
print(Hero.jumlah)
