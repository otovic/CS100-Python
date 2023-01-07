a = 'mama mama ima mama'

pon = [x for x in a]
counts = {}
for word in pon:
    counts.setdefault(word, 0)
    counts[word] += 1

for c, o in counts.items():
    print(str(c) + " " + str(o))