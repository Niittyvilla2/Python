kauttajatunnus = input("Anna käyttäjätunnus: \n")
salasana = input("Anna salasana: \n")
yritys = int(1)
oikea_kauttajatunnus = "python"
oikea_salasana = "rules"
while kauttajatunnus!= oikea_kauttajatunnus or salasana!=oikea_salasana:
    yritys = yritys+1
    print("Pääsy evätty \n")
    if yritys>5:
        break
    kauttajatunnus = input("Anna käyttäjätunnus: \n")
    salasana = input("Anna salasana: \n")
if kauttajatunnus==oikea_kauttajatunnus and salasana==oikea_salasana:
    print("Tervetuloa \n")