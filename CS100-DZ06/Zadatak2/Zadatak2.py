# Napisati program koji na postojeću tekstualnu datoteku unosi n redova teksta. 
# Tekst se unosi red po red preko standardnog ulaza. 
# Prikazati sve redove teksta na standardnom izlazu. 
# Ne koristiti kontekstni menadžer.

file = open('text.txt', 'w+')

n = int(input("Broj redova koji se unose -> "))

for x in range(n):
    file.write(str(input("Tekst za upis -> ")) + "\n") if n - x > 1 else file.write(str(input("Tekst za upis -> "))) #proveravam ako je zadnji red, ako jeste onda ne ispisujem \n kako ne bi imao prazan red na kraju

file.close()
file = open('text.txt', 'r')
print(file.read())

file.close()