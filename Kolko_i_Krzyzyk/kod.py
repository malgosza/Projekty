class poleGRY:
    def __init__(self):
        self.plansza=[]
    def wypelnijPlansze(self):
        for x in range(0,9):
            self.plansza.append(0)
        print(self.plansza)

p=poleGRY()
p.wypelnijPlansze()


