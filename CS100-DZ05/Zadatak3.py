# Napisati funkciju koja izračunava zapreminu sfere prema njenom poluprečniku.

zapreminaSfere = lambda pp: 4*(pp*pp*pp)*3.14 / 3
print("Zapremina sfere je -> " + str(zapreminaSfere(int(input("Unesite poluprecnik -> ")))))