# Napisati program koji proverava ispravnost jmbg-a. 
# Jmbg je ispravan ako ima 13 cifara. U jmbg-u se ne sme sadržati slovo niti bilo koji drugi karakter. 
# Obezbediti da korisnik vrši proveru jmbg-ova sve dok ne unese reč ‘kraj’. 
# Ukoliko unese neispravan jmbg izbaciti izuzetak.

while True:
    try:
        jmbg = str(input("Unesite jmbg -> "))
        if jmbg.lower() == "kraj":
            break

        if(any(not slovo.isdigit() for slovo in jmbg)):
            raise Exception("JMBG ne moze sadrzati karaktere koji nisu brojevi!")
        elif len(jmbg) != 13:
            raise Exception("JMBG mora biti duzine 13 karaktera!")

    except Exception as error:
        print(error)

    