import unittest


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