# Napisati funkciju za kreiranje i štampanje brojeva gde su vrednosti kvadrat brojeva između
# od 1 do (zaključno sa) 30.

def squareOfNumbers():
    for x in range(1, 31):
        print(f"{x} na kvadrat -> {x*x}")

squareOfNumbers()