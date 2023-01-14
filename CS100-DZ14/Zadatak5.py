# Napišite klasu Geometrija sa podrazumevanim konstruktorom bez parametara.
# Napišite metodu u klasi Geometrija koja se zove distanca() koja omogućava da se
# izračuna rastojanje između dve tačke A = (a1, a2), B = (b1, b2) (neka tačka M se
# identifikuje sa svojim parom koordinata M = (k, i)).
# Napišite metodu u klasi Geometrija koja se zove sredina() koja omogućava
# određivanje sredine trougla (gde se presecaju srednje linije trougla).
# Napišite metod koji se zove obim() koji omogućava izračunavanje obima trougla
# Napišite metod pod nazivom paralelogram() koji vraća True ako je trougao
# paralelogram i False ako nije.

import math

class Gemoterija:
    def __init__(self) -> None:
        pass

    def distanca(self, A, B):
        print(f"M ({math.sqrt((A[0] - B[0])*(A[0] - B[0]))}, {math.sqrt((A[1] - B[1])*(A[1] - B[1]))})")

    def sredina(self, A, B ,C):
        print(f"Centar trougla: {(A[0] + B[0] + C[0]) / 3}, {(A[1] + B[1] + C[1]) / 3}")


a = Gemoterija()
a.distanca((5, 1), (2, 3))
a.sredina((1, 2), (3, 4), (5, 5))