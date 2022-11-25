n = int(input("Broj brojeva -> "))
listaBrojeva = []

while len(listaBrojeva) < n:
    listaBrojeva.append(int(input("Unesite broj -> ")))

listaBrojeva.remove(max(listaBrojeva))
listaBrojeva.remove(min(listaBrojeva))
listaBrojeva.sort()

print(listaBrojeva)