class Hero:

    def __init__(self, name, health, attackpower, armornumber):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.armourNumber = armornumber

    def serang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.attackpower)

    def diserang(self, lawan, attackpower_lawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackpower_lawan / self.armourNumber
        print('serangan terasa\t:' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))


sniper = Hero('sniper', 100, 10, 5)
rikimaru = Hero('rikimaru', 100, 20, 10)

sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)
print("\n")
rikimaru.serang(sniper)