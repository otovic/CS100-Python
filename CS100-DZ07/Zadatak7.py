# Napisati program koji proverava da li je uneti broj prost. 
# Koristiti posebne funkcije za unos, obradu (proveru da li je broj prost) i štampu rezultat. 
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

def isProst(broj):
    if any(broj % delilac == 0 and broj != delilac for delilac in range(2, 10)):
        return "nije prost broj"
    else:
        return "Prost broj"

def stampaj(text):
    print(text)

stampaj(isProst(unosBroja()))