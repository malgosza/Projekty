import json

def deserializeJson():
    x='''
    {
        "imie":"Ala",
        "nazwisko":"Kowalski",
        "wiek": 12,
        "adres": {
            "miasto":"Gdansk",
            "ulica":"Fiokowa"
        },
        "auta":["opel","volvo"]
    }
    '''
    # serializowac->wynik to json, deserialize-> wejscie to json
    slownik=json.loads(x)
    print(slownik["nazwisko"])
    print(slownik["adres"]["miasto"])
    print(slownik["auta"][0])

def serializeJson():
    slownik={"klasa":1,"Nauczyciel":{"imie":"Anna","Nazwisko":"Kowalska"},"szkola":"Abrahama","ilosc":13,"dzieci":["Marysia","Jan"]}
    nowyJson=json.dumps(slownik)
    print(nowyJson)

def serializeJsonToFile():
    slownik={"klasa":1,"Nauczyciel":{"imie":"Anna","Nazwisko":"Kowalska"},"szkola":"Abrahama","ilosc":13,"dzieci":["Marysia","Jan"]}
    plik=open('test.json','w')
    json.dump(slownik,plik)
    plik.close()

def jsonToDict():
    with open('test.json') as plik:
        slownik=json.load(plik)
        print(slownik["szkola"])    

jsonToDict()