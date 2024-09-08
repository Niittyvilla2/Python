import random

def noppa(sivu):
    luku = random.randint(1,6)
    return luku
sivu=int(input("Nopan sivujen määrä: \n"))
print("")
numero = 0
while numero != sivu:
    numero = noppa(sivu)
    print(numero)
