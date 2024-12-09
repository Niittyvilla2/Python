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


class Kilpailu:
    def __init__(self, pituus, kNimi, autot: list):
        self.autot = autot
        self.pituus = pituus
        self.knimi = kNimi

    def tunti_kuluu(self):
        #kiihdytys
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))

        #matka
        for auto in autot:
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in autot:
                auto = [auto.rekkari, auto.maxnopus, auto.nopeus, auto.kuljettumatka]
                print(auto)

    def kilpailu_ohi(self,):
        pituus = self.pituus
        for auto in autot:
            if auto.kuljettumatka > self.pituus:
                return True


#Autot
autot = []

for i in range(10):
    auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    autot.append(auto)
