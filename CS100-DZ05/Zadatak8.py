# Napisati funkciju calc_distance(x1, x2, y1, y2) koja će izračunati i vratiti rastojanje između
# dve tačke dvodimenzionalnoj osi.
import math

def calc_distance(x1, x2, y1, y2):
    return math.sqrt(((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1)))

x1 = int(input("x1 -> "))
y1 = int(input("y1 -> "))
x2 = int(input("x2 -> "))
y2 = int(input("y2 -> "))
print(calc_distance(x1, x2, y1, y2))
