from abc import ABC, abstractmethod


class Hewan(ABC):
    @abstractmethod
    def bersuara(self):
        pass


class Kucing(Hewan):
    def bersuara(self):
        print("Meooow")


class Anjing(Hewan):
    def bersuara(self):
        print('Goook gook gokk')


kucingku = Kucing()
kucingku.bersuara()

anjingku = Anjing()
anjingku.bersuara()
