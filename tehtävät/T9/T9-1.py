# Auto luokka
class Auto:
    def __init__(self, rekkari, maxnopeus):
        self.rekkari = rekkari
        self.maxnopus = maxnopeus
        self.nopeus = 0
        self.kuljettumatka = 0
        pass


#Luodaan uusi auto
auto1 = Auto("ABC-123", 142)

#Printataan auton ominaisuudet ja muistetaan yksiköt
print(f"Rekkari: {auto1.rekkari}")
print(f"Maximi nopeus: {auto1.maxnopus} km/h")
print(f"Tämänhetkinen nopeus: {auto1.nopeus} km/h")
print(f"Kuljettu matka: {auto1.kuljettumatka} km")