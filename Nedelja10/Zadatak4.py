a = 'ovo je neki test da vidim da li ce da radi 123@#!#$324!$@41414@$($_@*)($&(#@$^*^#@%&'

pon = [x for x in a]
counts = {}
for word in pon:
    counts.setdefault(word, 0)
    counts[word] += 1

for c, o in counts.items():
    print(str(c) + " " + str(o))