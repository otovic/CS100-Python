# Napisati korisnički interaktivni program za izračunavanje količine sagorenih kalorija.
# Tražiti masu osobe u kg, a računati u težinskim funtama (kg * 0.453592); obavezno koristite
# deskriptivni prompt tako korisnik zna šta da unese.
# Tražiti pređenu kilometražu, a računati pređeni put u miljama (km * 1.609);
# Izračunajte potrošene kalorije koristeći formulu ispod:
# Sagorele kalorije su težina osobe u funtama pomnožena udaljenost koju je pretrčala u
# miljama, pa sve pomnoženo konstantom od 0.653.
# Uraditi verifikaciju ulaza za negativne unete vrednosti.

def potroseneKalorije(kilaza, kilometraza):
    return ((kilaza * 0.453592) * (kilometraza * 1.609)) * 0.653

masa = float(input("Vasa kilaza (kg) -> "))
predjenaKm = 0
if masa < 1:
    print("Unesite odgovarajucu kilazu!")
else:
    predjenaKm = float(input("Predjena kilometraza -> "))
    if predjenaKm < 0:
        print("Unesite ispravnu kilometrazu!")
    else:
        print("Ukupno ste sagoreli ->" + str(potroseneKalorije(masa, predjenaKm)))

