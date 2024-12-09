import random
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


class Sahkoauto(Auto):
    def __init__(self, rekkari, maxnopeus, akku):
        #akkukapasiteetti kilowattitunteina
        self.akku = akku
        super().__init__(rekkari, maxnopeus)


class Polttomoottoriauto(Auto):
    def __init__(self, rekkari, maxnopeus, tankki):
        #bensatankin koko litroina
        self.tankki = tankki
        super().__init__(rekkari, maxnopeus)


#Autot
sAuto = Sahkoauto("ABC-15", 180, "52.5 kWh")
pAuto = Polttomoottoriauto("ACD-123", 165, "32.3 l")

#Ajo
sAuto.kiihdyta(random.randint(100, 180))
pAuto.kiihdyta(random.randint(100, 165))
sAuto.kulje(3)
pAuto.kulje(3)

print(f"Polttomoottoriauton kuljettu matka: {pAuto.kuljettumatka}")
print(f"Sähköauton kuljettu matka: {sAuto.kuljettumatka}")