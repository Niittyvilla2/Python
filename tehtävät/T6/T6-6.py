from math import pi
def pizza(halkaisija, hinta):
    r=halkaisija/2
    a=pi*r**2
    ha = hinta/a
    return ha
halkaisija1 = int(input("Anna ensimmäisen pizzan halkaisija: \n"))
hinta1 = int(input("Anna ensimmäisen pizzan hinta: \n"))

halkaisija2 = int(input("Anna toisen pizzan halkaisija: \n"))
hinta2 = int(input("Anna toisen pizzan hinta: \n"))

if pizza(halkaisija1, hinta1)<pizza(halkaisija2, hinta2):
    print("Ensimmäinen pizza on halvempi.")
else:
    print("Toinen pizza on halvempi.")