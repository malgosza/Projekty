import unittest

# prosta klasa
class piesek:
    # konstruktor
    def __init__(self, imiePieska):
        self.imie = imiePieska

    def metoda(self):
        print("piesek ma na imie " + self.imie)

# uzycie
# p = piesek("azor")
# p.metoda()


# funkcja do przetestowania
def funkcja(a, b):
    return a+b


# klasa testowa
class TestDodawania(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, funkcja(1,2))


# odpalanie skryptu
if __name__ == "__main__":
    unittest.main()