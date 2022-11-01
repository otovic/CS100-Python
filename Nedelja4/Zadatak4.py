outputStr = ''

for x in range(0, 6):
    outputStr = ""
    for y in range(0, 6):
        if y == 0 or y == 6 - 1 or x == y or x + y == 6 - 1:
            outputStr += "*"
        else:
            outputStr += " "
    outputStr += " "
    print(outputStr) 

step = 0

print("\n")

outputStr = ""

for x in range (0, 7):
    outputStr += ("*" + (" " * step) + "*")
    step += 1
    print(outputStr)
    outputStr = ""

