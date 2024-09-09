lentoasemat = {"Helsinki-Vantaan lentoasema":"EFHK", "Oulun lentoasema":"EFOU"}

while True:
    print("Jos haluat syöttää uuden lentoaseman kirjoita A")
    print("Jos haluat etsiä olemassa olevan lentoaseman tiedot kirjoita B")
    print("Jos haluat lopettaa kirjoita STOP")
    komento = input("\n")
    if komento == "A":
        uusi_nimi = input("Anna uuden lentokentän nimi: \n")
        uusi_numero = input("Anna uuden lentokentän ICAO-koodi: \n")
        lentoasemat[uusi_nimi] = uusi_numero
        print("Asema lisätty!\n")
    
    elif komento == "B":
        nimi=input("Anna lentokentän nimi: \n")
        if nimi in lentoasemat:
            print(f"Lentoaseman {nimi} ICAO-koodi on {lentoasemat[nimi]}\n")
        else:
            print("Lentoasema ei löydetty. \n")
    elif komento == "STOP":
        break
    else:
        print("Komento ei tunnistettu, yritä uudelleen. \n")
print("Ohjelman suoritus lopetettu!")