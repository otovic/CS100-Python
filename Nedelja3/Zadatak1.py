month = int(input("Mesec: "))

if month < 1 or month > 12:
    print("Unesite ispravan broj meseci!")
elif month >= 1 and month < 4:
    print("Prvi kvartal")
elif month >= 4 and month < 7:
    print("Drugi kvartal")
elif month >= 7 and month < 10:
    print("Treci kvartal")
else:
    print("Cetvrti kvartal")
