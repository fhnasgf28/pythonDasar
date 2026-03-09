class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showinfo(self):
        print("ShowInfo di class hero")
        print("{} health: {}".format(
            self.name,
            self.health
        )
        )


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    #     override
    def showinfo(self):
        print('showinfo di subclass Hero_intelligent')
        print("{} \n\tTipe: intelligent, \n\thealth: {}".format(self.name, self.health))


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 2009)


lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showinfo()
