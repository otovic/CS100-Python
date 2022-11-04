# Napisati funkciju koja uzima tekst i šifruje ga Cezarovom šifrom. Svako slovo u tekstu se
# zamenjuje slovom na određenom broju mesta dalje u abecedi. Funkcija prima tekst i broj za
# koji se pomeraju slova.
# Primer:
# broj za pomeranje: 2
# A -> C 
# B -> D
# C -> E
# D -> F
# X -> Z
# Y -> A
# Z -> B

def cezarovaSifra(text, pomeraj):
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cypher = ""

    for x in text.upper():
        cypher += abc[abc.index(x) + pomeraj] if abc.index(x) + pomeraj <= 25 else abc[(abc.index(x) + pomeraj - 1) % 25]
    
    print("Sifriran tekst -> " + cypher)

cezarovaSifra(str(input("Unesite tekst za sifriranje -> ")), int(input("Unesite pomeraj -> ")))