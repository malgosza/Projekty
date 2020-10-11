from random import randint

# print('Zgadnij liczbe od 0 do 10')
# x=int(input()) #1
# y=randint(1,10) #5
# while x!=y:
#     if x<y:
#         print('Za mala liczba')
#     elif x>y:
#         print('Za duza liczba')            
#     x=int(input())     
# print('OK! Zgadles')             

def validate(x):
    if len(x)!=3:
        raise Exception(f'Nieprawidlowa liczba, Podano zly rozmiar: {len(x)}')
    elif x[0]!='a':
        raise Exception(f'Nie zaczyna sie od \'a\', zaczyna sie od {x[0]}')
    elif x[len(x)-1]!='z':
        raise Exception(f'Nie konczy sie na \'z\', konczy sie na {x[len(x)-1]}')



x=input('Podaj slowo: ')
try:
    validate(x)
    print('OK!')
except Exception as e: 
    print(e)

  