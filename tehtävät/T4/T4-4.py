import random
numero = input("Anna numero 1 ja 10 välillä: \n")
vastaus = random.randint(1,10)

while int(numero)!=vastaus:
    if int(numero)>vastaus:
        print("Liian suuri!")
    if int(numero)<vastaus:
        print("Liian pieni!")
    numero = input("Anna numero 1 ja 10 välillä: \n")
print("Oikein!")