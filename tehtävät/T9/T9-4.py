import random
# Auto luokka
class Auto:
    def __init__(self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopus = maxnopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdyta(self, kmh):
        if kmh + self.nopeus > 0 and kmh + self.nopeus < self.maxnopus:
            self.nopeus = self.nopeus + kmh
        elif kmh + self.nopeus < 0:
            self.nopeus = 0
        elif kmh + self.nopeus > self.maxnopus:
            self.nopeus = self.maxnopus
    
    def kulje(self, aika):
        if aika > 0:
            matka = aika * self.nopeus
            self.kuljettumatka = self.kuljettumatka + matka


#Autotttt
auto1 = Auto("ABC-1", random.randint(100,200))
auto2 = Auto("ABC-2", random.randint(100,200))
auto3 = Auto("ABC-3", random.randint(100,200))
auto4 = Auto("ABC-4", random.randint(100,200))
auto5 = Auto("ABC-5", random.randint(100,200))
auto6 = Auto("ABC-6", random.randint(100,200))
auto7 = Auto("ABC-7", random.randint(100,200))
auto8 = Auto("ABC-8", random.randint(100,200))
auto9 = Auto("ABC-9", random.randint(100,200))
auto10 = Auto("ABC-10", random.randint(100,200))

auto1.kiihdyta(random.randint(-10,15))
auto1.kulje(1)
