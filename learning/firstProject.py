tab=[("ser",41),
("sok",25),
("miod",32)]
suma=0
for z in tab:
    # suma+=z
    suma=suma+z[1]

slownik={}
for x in tab:
    # str zamienia typ na stringa
    prop=x[1]*100/suma
    print(x[0]+ ' -> ' +str(prop))
    slownik[x[0]]=prop

#krotka ma niezmienna dlugosc i moze trzymac elementy roznego typu
krotka=("ser", 20)

# slownik
print(slownik)
# mozna przeciazac operatory np. + 



for klucz in slownik:
    # 40>slownik[klucz]>30
    if slownik[klucz]>30 and slownik[klucz]<40:
        print(klucz)

a="kotel"
b="piesem"
a,b=b,a
print(a + b)
c=9
d=10
print(f"{a} ma {c}, a {b} ma {d} ")


# list comprehensions
# while
# if, elif, else

# fizz buzz \/
#  zwroc liste unikalnych stringow - zwroc stringa bez powrtorek
# szyfr cezara \/
# policz wysapienia lister w slowie (dict) \/
# czytanie z pliku

# hello world selenium python

# klasy, polimorfizm
# importy (np. jsons, math)