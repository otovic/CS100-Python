# Napisati program koji traži od korisnika da unese 10 pozitivnih celih brojeva. 
# Program pronalazi najmanji broj i prikazuje ga na ekranu. 
# Ukoliko korisnik unese broj koji nije pozitivan izbaciti izuzetak. 
# Ukoliko unos nije validan takođe će se desiti izuzetak.
brojac = 0
brojevi = []

while brojac < 10:
    try:
        broj = input("Unesite broj -> ")
        if (broj == "" or any(not slovo.isnumeric() for slovo in broj)) or (int(broj) < 0):
            raise Exception("Unesite ispravan broj!")
        else:
            brojac += 1
            brojevi.append(int(broj))

    except Exception as error:
        print(error)

print("Najmanji broj je -> " + str(min(brojevi)))