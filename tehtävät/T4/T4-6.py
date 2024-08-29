# π≈4n/N on on ympyrän sisällä olevat pisteet ja N on kaikki pisteet
# epäyhtälöllä x^2+y^2<1 testataan onko yksittäinen piste ympyrän sisällä

import random
import math
interactor = 0
N = input("Anna arvottavien pisteiden määrä: ") # pisteiden kokonaismäärä
n = 0 # ympyrän sisään osuvat pisteet
while interactor < N:
    interactor += 1
    # kaksi eri tapaa arpoa 1 ja -1 välillä
    x = random.random()*2-1
    y = random.uniform(-1, 1)
    print(f"Satunnainen piste: {x}, {y}")
    if x**2 + y**2 < 1:
        print("Osui ympyrän sisälle.")
        n = n + 1
print(f"{N} pisteestä {n} osui yksikköympyrän sisälle.")
result = 4 * n / N
print(f"Piin likiarvo on {result}")
print(f"Virhe verrattuna math.pi: ({math.pi:.5f}): {result- math.pi:.5f}")