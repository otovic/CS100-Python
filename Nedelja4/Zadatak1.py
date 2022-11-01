numberOfBugs = 0
totalBugs = 0

for x in range(1, 6):
    numberOfBugs = int(input(f"Broj bagova {x} dana -> "))
    totalBugs += numberOfBugs

print(f"Za 5 dana imali smo {totalBugs} bagova!")