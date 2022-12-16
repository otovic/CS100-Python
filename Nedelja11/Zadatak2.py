reci = set()
text = input("Unesite neki tekst: ").split()
dict = {}
for rec in text:
    dict.setdefault(rec.lower(), 0)
    dict[rec] += 1

for x, y in dict.items():
    if y == 1:
        reci.add(x)

print(reci)