def listy():
    lista=list(range(10))
    print(lista)

    # list comprehension
    lista = [i for i in range(10)]
    print(lista)

    listaZer=[0 for i in range(10)]

    print(lista[4:6])
    print(lista[-1])
    print("AlaMaKot"[-1])


    tablica=[0,"zero","562"]
    print(tablica)

def generatory():
    print("generuje...")
    x=range(100000000000000000000)  # stworzony szblon tablicy, a nie CALA tablica, dane strumieniowane
    print("wygenerowal!")
    # x[234] nie zadziala!
    for i in x:
        print(i)

# yield szybko dziala, bo nie ma zbednych obliczen; wykonujemy obliczenia tylko wtedy jak ich potrzebujemy
def generuj(ile):
    print("zaczynam generowanie!")
    for i in range(ile):
        print("DLUGA OPERACJA")
        yield i # return w przyszlosci (w momencie wywolania nextem)
    print("skonczylem!")
    # raise StopIteration()

# jednolinijkowy generator (przerobiony z list comprehension)
# lista = (i for i in range(10))

a = generuj(4)

print("startujemy")
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a)) 
# print(next(a)) # StopIteration exception!
# print(next(a))
# print(next(a))

for i in a:
    print(i)

def generujNieskonczonosc():
    i = 0
    while True:
        yield i
        i += 1

x = generujNieskonczonosc()
print(next(x))
print(next(x))

