lista = []
for i in range (10):
    liczba = int(input(f'podaj liczbe {i + 1} : '))
    lista.append(liczba)

    print("lista:", lista)
    print("max wartosc", max(lista))
    print("min wartosc", min(lista))

