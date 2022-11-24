# Napisati program koji množi samo neparne brojeve. 
# Program traži od korisnika da unosi samo neparne brojeve. 
# Ukoliko korisnik unese paran broj, prekida se rad programa i na ekranu se prikazuje proizvod unetih brojeva. 
# Ukoliko je nekorektan ulaz ili korisnik unese nulu treba izbaciti izuzetak. 
proizvod = 0

while True:
    try:
        broj = int(input("Unesite neparan broj -> "))
        if broj % 2 == 0:
            print(proizvod)
            break
        else:
            proizvod *= broj
    except ValueError:
        print("Unesite ispravan broj!")
