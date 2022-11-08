# Napisati program koji najpre ispisuje sve reči iz datoteke po redovima. 
# Zatim, preko standardnog ulaza ubaciti koju reč treba promeniti u n-tom redu, 
# i ubaciti novu reč koja menja postojeću reč u datoteci. 
# Ne koristiti kontekstni menadžer.

file = open("text.txt", 'r')
lines = file.readlines()

for x in range(len(lines)):
    print(f"{x + 1}: " + lines[x].replace("\n", ''))

file.close()

n = int(input("Koji red zelite zameniti -> "))

if n > len(lines):
    print("Unesite broj koi nije veci od samog broja redova!")
else:
    rec = str(input("Koju rec zelite da ubacite -> "))

    file = open("text.txt", "w")
    file.write("")

    lines[n - 1] = rec + '\n' if n - 1 != len(lines) - 1 else rec #menjam n-tu rec u listi sa novim redom na kraju ako nije zadnja rec, ako je zadnja onda ne dodajem \n kako ne bi imao prazan red na kraju

    for x in range(len(lines)):
        file.writelines(lines[x])

    file.close()

    file = open("text.txt", 'r')
    print("Fajl posle promene: \n" + file.read())
    file.close()