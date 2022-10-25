# Napisati program koji broji kalorije. Ljudski organizam tokom vežbanja sagori 4.2 kalorije u
# minutu. Program treba da prikaže koliko telo sagori kalorija nakon 10, 15, 20, 25 i 30 minuta
# vežbanja. Koristiti petlju.

for x in range(10, 31, 5):
    print("Za " + str(x) + " minuta sagoreno je: " + str(x * 4.2) + " kalorija!")
