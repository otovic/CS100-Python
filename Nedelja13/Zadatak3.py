def nadjiSumu(lista):
    suma = 0
    for index, vrednost in enumerate(lista):
        suma += vrednost
        print(f"{index}: {suma - vrednost} + {vrednost} = {suma}")
    return suma

lista = [1, 2, 3, 4, 5,]
print(f"Ukupno: {nadjiSumu(lista)}")