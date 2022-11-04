# Napisati funkciju koja izračunava zapreminu sfere prema njenom poluprečniku.

zapreminaSfere = lambda pp: 4*(pp*pp*pp)*3.14 / 3
poluprecnik = float(input("Unesite poluprecnik -> "))
print("Zapremina sfere je -> " + str(zapreminaSfere(poluprecnik)))