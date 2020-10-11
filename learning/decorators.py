# # nie ma NULL jest NONE
# x=None
# if x==None:
#     print("xd")
# if x is None:
#     print("Ole")    

def wykonaj(funkcja):
    x=1
    print("Przed wykonaniem")
    wynik = funkcja(x)
    print(f"po wykonaniu {wynik}")

@wykonaj
def inc(x):
    return x+1

@wykonaj
def dec(x):
    return x-1

print(inc(1))