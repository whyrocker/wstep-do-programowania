lista=[]

for i in range(10):
    element=input(f"element {i+1}:")
    lista.append(element)
    print("lista", lista)
    szukany=input("podaj element do wyszukiwania")
    ile= lista.count(szukany)
    print("element wystepuje", ile , "razy")
    indeks= int(input("podaj indeks do usuniecia:"))
    usuniety=lista.pop(indeks)
    print("usuniety element", usuniety)
    print("nowa lista", lista)