from geopy.distance import geodesic
import mysql.connector

def getGPS(icao):
    icao.upper()
    sql = f"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident = '{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    sijainti = kursori.fetchall()
    sijainti = (float(sijainti[0][1]), float(sijainti[0][2]))
    return sijainti

yhteys = mysql.connector.connect(
         host='localhost',
         port= 3306,
         database='flight_game',
         user='leksa',
         password='tapani',
         autocommit=True
         )

icao1 = input("Anna lähtö lentokentän ICAO-koodi: ")
icao2 = input("Anna saapumis lentokentän ICAO-koodi: ")
s1 = getGPS(icao1)
s2 = getGPS(icao2)
dist = geodesic(s1, s2).km
print(dist)
print(f"Kenttien välinen etäisyys on {round(dist, 2)}km")