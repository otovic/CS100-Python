def oipKvadrata(stranica):
    return str(stranica * stranica), str(4 * stranica)
    
p, o = oipKvadrata(5)

print("Obim je -> " + o + ", Povrsina je -> " + p)