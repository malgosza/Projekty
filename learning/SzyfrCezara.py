slowo="XYZABC"
noweSlowo=""
klucz=6
for i in range(len(slowo)):
    if (ord(slowo[i]) + klucz)>90:
        noweSlowo+=chr(ord(slowo[i]) + klucz-26)
    else:
        noweSlowo+=chr(ord(slowo[i]) + klucz)
print(noweSlowo)   
