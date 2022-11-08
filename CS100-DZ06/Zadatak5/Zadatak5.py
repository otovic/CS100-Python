# Napisati program koji kopira binarnu datoteku po blokovima. 
# Veličina bloka se unosi preko standardnog ulaza i dozvoljene vrednosti su: 
# 1024, 2048, 4096, 8192. Ukoliko korisnik ne unese neku od ovih vrednosti, vratiti poruku sa greškom. 
# Koristiti kontekstni menadžer.

validNums = [1024, 2048, 4096, 8192]
velBloka = int(input("Unesite velicinu bloka (1024, 2048, 4096 ili 8192 -> "))

if velBloka not in validNums:
    print("Unesite validnu velicinu bloka!")
else:
    with open("poodle.jpg", "rb") as rf:
        with open("poodleCopy.jpg", "wb") as wf:
            x = rf.read(velBloka)
            while len(x) > 0:
                wf.write(x)
                x = rf.read(velBloka)

rf.close()
wf.close()