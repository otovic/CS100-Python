def sumaElem(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sumaElem(lst[1:])

print(sumaElem([1, 2, 3, 4]))
