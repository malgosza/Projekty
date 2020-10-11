class Pies:
    # pierwszy argument KAZDEJ metody w klasie musi przyjmowac 'self', chyba ze jest statyczna
    def szczek(self):
        print('Szczek szczek')
    
    # zalezy co robimy w srodku to sie Python domysli albo nie (typowanie dynamiczne)
    def hau(self, ile):
        # zawsze do rzeczy ze srpdka odnosze sie przez self
        self.szczek()
        print(f'Szczeka {ile}')

class Kot:
    def __init__(self, imie):
        self.imie=imie

    def miau(self):
        print('Kot ' + self.imie)
        # nie ma przeciazania metod

class Hugo(Kot):
    # konstruktory sa dziedziczone, nie tak jak w Javie
    def jesc(self):
        print('Jem')

        
class Baron(Kot):
    def __init__(self):
        super().__init__('Baron')
        # self._iloscLap  -> protected
        # self.__iloscLap -> private

    def miau(self):
        print(4555)    

# metoda private 
    def __iloscLap(self):
        print(5)

    def __str__(self):
        return 'Jestem potworem'


if __name__ == "__main__":
    # pies=Pies()
    # pies.szczek()
    # pies.hau(5)
    # pies.hau('piec')

    # kot=Kot('garfild')
    # kot.miau()

    # hugus=Hugo('Hugo')
    # hugus.miau()
    # hugus.jesc()

    baron=Baron()
    baron.miau()

    # print(baron.__str__())
    print(baron)
    x=str(baron)
    print(x)

