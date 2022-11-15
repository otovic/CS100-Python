# Napisati program koji proverava da korisnik sme da uđe na žurku tako što ga pita koliko ima godina. 
# Samo punoletni korisnici imaju dozvolu za ulazak. 
# Maksimalan broj ljudi koji može da prisustvuje žurki je 20. 
# Ukoliko je korisnik maloletan izbaciti izuzetak.
brojGostiju = 0

while brojGostiju < 20:
    try:
        godine = int(input("Vas broj godina -> "))
        if godine > 17:
            brojGostiju += 1
        else:
            raise Exception("Morate biti punoletni! Dovidjena!")
    except ValueError:
        print("Unesite ispravan broj")
    except Exception as error:
        print(error)