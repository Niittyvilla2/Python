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

def lentoasema(code):
    connection = yhteys()
    sql = f"SELECT name, municipality FROM airport WHERE ident='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    vastaus_jono = cursor.fetchone()
    return vastaus_jono

koodi = input("Anna ICAO koodi: \n")
koodi = koodi.upper()
vastaus = lentoasema(koodi)

if vastaus:
    print(f"Haettu kenttä: {vastaus[0]}")
    print(f"Haettu sijaintikunta: {vastaus[1]}")
else:
    print("Lentoasemaa ei löydy.")