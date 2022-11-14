# Napisati program koji kopira binarnu datoteku po blokovima od 1024. 
# Korisnik unosi novo ime datoteke preko standardnog ulaza.
# Koristiti kontekstni menadžer.
imeDatoteke = str(input("Unesite ime datoteke -> "))

with open("copyfile.py", "rb") as rf:
    with open(imeDatoteke, "wb") as wf:
        x = rf.read(1024)
        while len(x) > 0:
            wf.write(x)
            x = rf.read(1024)
