# Napisati program koji proverava da li je uneti broj deljiv sa 7. 
# Koristiti posebne funkcije za unos, obradu (proveru da li je deljiv sa 7) i štampu rezultat. 
# Ukoliko je uneti broj nije ceo ili nije korektno unet izbaciti izuzetak.

def unosBroja():
    broj = 1.5
    try:
        while broj == 1.5:
            try:
                broj = int(input("Unesite broj -> "))
            except ValueError:
                print("Unesite ispravan broj!")
                broj = 1.5
    finally:
        return broj


def brojDeljiv(broj):
    return "Broj je deljiv sa 7!" if broj % 7 == 0 else "Broj nije deljiv sa 7!"

def stampaj(text):
    print(text)

stampaj(brojDeljiv(unosBroja()))           