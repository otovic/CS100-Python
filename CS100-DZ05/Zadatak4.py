# Napisati funkciju koja prihvata string i vraća broj velikih i malih slova u strungu.

def countLowerUpperCase(text):
    lowerCase = 0
    upperCase = 0

    for x in text:
        if not x.isupper():
            lowerCase += 1
        else:
            upperCase += 1
    
    return upperCase, lowerCase

upper, lower = countLowerUpperCase("PetarOtovic")
print(f"Ukupno velikih slova -> {upper}, ukupno malih slova -> {lower}")
