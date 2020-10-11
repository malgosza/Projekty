class MojInterface:
    def abc(self):
        raise Exception('implement me')
    def xyz(self):
        pass # "zamknieta klamra", pusta metoda

class MojaImplementacja(MojInterface):
    pass # teraz recznie zaimplementowac metody po javowemu

