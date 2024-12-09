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

    def tunti_kuluu(self, aika):
        #kiihdytys
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
        #matka
        for auto in self.autot:
            auto.kulje(aika)

    def tulosta_tilanne(self):
        for auto in self.autot:
                auto = [auto.rekkari, auto.maxnopus, auto.nopeus, auto.kuljettumatka]
                print(auto)

    def kilpailu_ohi(self):
        for auto in autot:
            if auto.kuljettumatka > self.pituus:
                return True
            else:
                return False


#Autot
autot = []

for i in range(10):
    auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    autot.append(auto)

#Kilpailu
sr = Kilpailu(8000, "Suuri romuralli", autot)
print("Suuri romiralli alkaa!\n")
while sr.kilpailu_ohi() == False:
    sr.tunti_kuluu(10)
    sr.kilpailu_ohi()
    print("\nTämän hetkinen tilanne \n")
    sr.tulosta_tilanne()

print("\nSuuri romuralli on päättynyt!")