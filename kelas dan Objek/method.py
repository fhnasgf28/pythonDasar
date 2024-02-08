class Hero:
    # class variabel
    jumlah_hero = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(f"namaku {self.name}")

    # method dengan argumen, tanpa return
    def healthUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('Sniper', 100, 90,80)
hero2 = Hero('Mirana', 100, 50, 50)

hero1.siapa()
hero2.siapa()

hero1.healthUp(10)
hero2.healthUp(20)

print(hero1.getHealth())
print(hero2.getHealth())