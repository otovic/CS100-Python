# Napisati funkciju koja od unetog stringa (minimalno 8 karaktera), pretvara sva mala slova u
# velika slova. Uraditi verifikaciju ulaza.

def ConvertUpper(text): 
    print(text.upper()) if len(text) > 7 else print("Unesite rec koja sadrzi minimalno 8 karaktera!")


text = str(input("Unesite rec od minimalno 8 karaktera -> "))
ConvertUpper(text)