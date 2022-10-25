# Napisati program koji prikazuje tabelu milja i kilometara, zaokruženo na dve decimale. Jedna
# milja je jednaka 1.60394 kilometara. Tabela se generiše uz pomoć petlje. Početna vrednost za
# koju se prikazuje vrednost u tabeli je 10, a poslednja 80 milja i vrednost za tabelu se generiše
# na svakih 10 milja. Odnosno vrednosti u tabeli su 10, 20, ... 80.
# Primer tabele:
# 10 milja -16.04 km
# 20 milja - 32.08 km

for x in range(10, 81, 10):
    print(str(x) + " milja - " + str(round(1.60394 * x, 2)) + "km")
