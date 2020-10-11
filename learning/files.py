# domyslnie plik do odczytu
def readFile():
    plik=open('SzyfrCezara.py')

    for linijka in plik:
        print(linijka)

    plik.close()

#  to jest bezpiecznejsze i autoclose
def contextReadFile():
    with open('SzyfrCezara.py') as plik:
        for linijka in plik:
            print(linijka)

# a-> append
def writeFile():
    with open('testowyPlik.txt','w') as plik:
        plik.writelines(['a','abc\n', 'Kot ma ale', '123456', ' '])



writeFile()        
