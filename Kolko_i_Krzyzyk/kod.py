class poleGRY:

    def __init__(self):
        self.plansza=[]
        self.KRZYZYK = 1
        self.KOLKO = 2
        self.czyTerazKrzyzyk = True

        for x in range(0, 9):
            self.plansza.append(0)

    def piszPlansze(self):
        for y in range(0,len(self.plansza)):
            if(y%3==0 and y!=0):
                print()
            print(self.plansza[y], end='')

    def ruchGracza(self, idx):
        aktualnaFigura = self.KOLKO
        if(self.czyTerazKrzyzyk == True):
            aktualnaFigura = self.KRZYZYK
            self.czyTerazKrzyzyk = False

        self.plansza[idx]= aktualnaFigura

    # zwraca 0 gdy gramy dalej
    # 1 gdy wygral krzyzyk
    # 2 gdy kolko
    # 3 gdy remis
    def wynikGry(self):
        pass



p=poleGRY()