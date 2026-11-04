a=float(input("podaj pierwsza liczbe:"))
b=float(input("podaj druga liczbe:"))
c=float(input("podaj trzecia liczbe:"))
najmniejsza = a
najwieksza = a
if  b < najmniejsza:
 najmniejsza = b
if c < najmniejsza:
 najmniejsza=c
if b > najwieksza:
 najwieksza=b
if c > najwieksza:
 najwieksza=c
print("najmniejsza liczba :",najmniejsza)
print("najwieksza liczba :",najwieksza)