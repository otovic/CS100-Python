# Napisati program koji najpre ispisuje sve reči iz datoteke po redovima. 
# Datoteka je takva da svaki red ima jednu reč. 
# Zatim, preko standardnog ulaza ubacivati (red po red) reči treba promeniti u postojećoj datoteci. 
# Koristiti kontekstni menadžer.

# rec1
# rec2
# rec3
# rec4

with open("text.txt", "r") as f:
    lines = f.readlines()

    for x in range(len(lines)):
        print(f"{x + 1}: " + lines[x].replace("\n", ''))

print("Unesite zamene za reci u fajlu: \n")

with open("text.txt", "w") as f:
    for x in range(len(lines)):
        if x < len(lines) - 1:
            f.write(str(input(f"{x + 1} rec za zamenu -> ")) + "\n")
        else:
            f.write(str(input(f"{x + 1} rec za zamenu -> ")))

with open("text.txt", "r") as f:
    print("Novi fajl: \n" + f.read())
