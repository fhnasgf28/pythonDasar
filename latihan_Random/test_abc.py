from abc import ABC, abstractmethod

class Hewan(ABC):
    @abstractmethod
    def bersuara(self):
        pass 

class Kucing(Hewan):
    def bersuara(self):
        return "Meong"

kucing_oren = Kucing()
print(kucing_oren.bersuara())