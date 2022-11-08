# Napisati za čitanje prvih n redova tekstualne datoteke. Prikazati tih n redova teksta na standardnom izlazu. 
# Ne koristiti kontekstni menadžer.

f = open("text.txt", 'r')

n = int(input("Broj redova za citanje -> "))
i = 0

fs = f.readlines()

while i < n:
    if i < len(fs): #proveravam da li i nije vece od broja redova, i ako nije stampam red
        print(fs[i].replace('\n', ''))
        i += 1
    else:
        i = n #ako je i vece od broja redova, zavrsavam while

f.close()