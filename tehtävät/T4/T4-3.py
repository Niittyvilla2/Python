pienin=int(0)
suurin=int(0)
numero = input("Anna numero: \n")
if numero!= "":
    pienin=int(numero)
    suurin=int(numero)
while numero!="":
    numero = input("Anna numero: \n")
    if numero == "":
        break
    numero = int(numero)
    if numero<pienin:
        pienin = numero
    if numero>suurin:
        suurin = numero
print("Pienin antamasi numero: " + str(pienin))
print("Suurin antamasi numero: " + str(suurin))