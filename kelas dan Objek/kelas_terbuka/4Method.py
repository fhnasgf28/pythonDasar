class Hero:

    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

        #void function, method tanpa return, tanpa argumen
    def siapa(self):
        print("namaku adalah" + self.name)

    #method dengan argumen, tanpa return
    def healthUp(self, up):
        self.health += up

    #method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero('sniper', 100, 19, 6)
hero2 = Hero('Mario Bros', 90, 20, 15)

hero1.siapa()
hero2.healthUp(10)

print(hero1.getHealth())