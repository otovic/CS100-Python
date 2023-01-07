def brojPonavljanja(x, n):
    if n < 10:
        if x == n:
            return 1
        else:
            return 0
    if x == n % 10:
        return 1 + brojPonavljanja(x, int(n / 10))
    else:
        return brojPonavljanja(x, int(n / 10))

print(brojPonavljanja(2, 112311))