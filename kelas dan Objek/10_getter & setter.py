class Hero:
    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('Armor di delet')
        self.__armor = None


sniper = Hero('sniper', 100, 10)

print('Merubah Info')
sniper.name = 'dadang'
print(sniper.info)
