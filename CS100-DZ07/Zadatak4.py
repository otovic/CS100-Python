# Napisati program koji od korisnika traži da unese 5 negativnih brojeva. 
# Program pronalazi najveći broj i prikazuje ga na ekranu. 
# Ukoliko korisnik unese broj koji nije negativan izbaciti izuzetak. 
# Ukoliko unos nije validan takođe će se desiti izuzetak.

brojac = 0
brojevi = []

while brojac < 5:
    try:
        broj = input("Unesite broj -> ")
        if "-" in broj:
            broj = broj.replace("-", "")
            if (any(not slovo.isdigit() for slovo in broj)) or int(broj) * -1 > -1:
                raise Exception("Unesite ispravan broj!")
            else:
                brojac += 1
                brojevi.append(int(broj) * -1)
        else:
            raise Exception("Unesite ispravan broj!")

    except Exception as error:
        print(error)

print("Najveci broj je -> " + str(max(brojevi)))