import pickle
x=int(input("Uneti koliko opstina ima?"))
opstine={}
for i in range(x):
    naziv=input("Uneti naziv opstine")
    kolicina_djubrista=input("Uneti kolicinu djubrista")
    opstine[naziv]=kolicina_djubrista
with  open ('listaopstina.pkl',"wb") as lo:
    pickle._dump(opstine,lo)
with open ('listaopstina.pkl','rb') as lo:
    lolist=pickle.load(lo)
print(lolist)