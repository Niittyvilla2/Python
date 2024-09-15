import mysql.connector

def yhteys():
    return mysql.connector.connect(
        host = "localhost",
        database = "flight_game",
        user = "root",
        password = "VerySecurePassw0rd",
        autocommit = True,
        collation = "utf8mb4_general_ci"
    )

def hell(list, element):
    for i in list:
        if i[0] == element:
            return list.index(i)
maakoodi = input("Anna maakoodi: \n")
maakoodi.upper()
connection = yhteys()
sql1 =f"SELECT iso_country, type FROM airport WHERE iso_country = '{maakoodi}'"
sql2 =f"SELECT DISTINCT type FROM airport"
lista = []
kursori = connection.cursor()
kursori.execute(sql1)
pod1 = kursori.fetchall()
kursori.execute(sql2)
pod2 = kursori.fetchall()

for type in pod2:
    lista.append([type[0], 0])

for type in pod2:
    for row in pod1:
        if row[1] == type[0]:
            p=hell(lista, type[0])
            lista[p][1]=lista[p][1]+1

for type in lista:
    print(f"{type[0]}: {type[1]}")