# Napisati program koji sastavlja rečenicu od unetih reči. 
# Korisnik sa tastature unosi 5 reči. Svaka reč mora imati najmanje 3 slova 
# i ne sme sadržati nijedan specijalan karakter sem znakova interpunkcije (, i . i ? i !). 
# Ukoliko reč nije ispravno uneta izbaciti izuzetak. 
# Na kraju program ispisuje celu rečenicu tako što reči odvoji razmakom i ispiše ih u jednom redu.
brojReci = 0
recenica = ""

while brojReci < 5:
    try:
        rec = str(input("Unesite rec -> "))
        if len(rec) > 2 and any(not slovo.isnumeric() or not slovo.isalpha() or slovo not in [",", ".", "?", "!"] for slovo in rec):
            brojReci += 1
            recenica += rec + " "
        else:
            raise Exception("Unesite ispravnu rec!")
    except Exception as error:
        print(error)
print(recenica)