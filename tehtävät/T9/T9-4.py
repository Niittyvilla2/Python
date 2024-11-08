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


#Autot
autot = []

for i in range(10):
    auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    autot.append(auto)

#Kilpailu
kilpailu = True
while kilpailu:
    #Kiihdytys
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
    #Matka
    for auto in autot:
        auto.kulje(1)
    #Katsotaan voittiko kukaan
    for auto in autot:
        if auto.kuljettumatka > 10000:
            kilpailu = False
            for auto in autot:
                auto = [auto.rekkari, auto.maxnopus, auto.nopeus, auto.kuljettumatka]
                print(auto)

