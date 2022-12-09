def getWords(words):
    array = [str(x).strip() for x in words.split(',')]
    array = [x.upper() for x in sorted(set(array))]
    print(array)

getWords('petar,petarrr,otttt,petar')