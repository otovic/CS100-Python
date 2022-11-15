# Napisati program koji računa obim kruga uz pomoć funkcije koja kao parametar prima prečnik kruga. 
# Ukoliko se za prečnik unese negativan broj ili nula izbaciti izuzetak. 
# Ukoliko unos nije validan takođe će se desiti izuzetak.

def obimKruga(precnik):
    try:
        if any(slovo.isalpha() for slovo in precnik) or int(precnik) < 1:
            raise Exception("Unesite ispravnu vrednost za precnik kruga!")
        else:
            return "Obim kruga je -> " + str(2*int(precnik)*3.14)
    except Exception as error:
        return error

print(obimKruga(input("Unesite precnik kruga -> ")))