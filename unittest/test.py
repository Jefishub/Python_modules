import unittest
"""
def add(x:int, y:int) -> int:
    return x+y

class SimpleTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(5,4),9)
"""

def add(x:int, y:int) -> int:
    return x+y

def tulo(x:int, y:int) -> int:
    return x*y

class SimpleTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(2,4),6)

    def test_add2(self):
        self.assertEqual(tulo(4,5),20)


    def test_add3(self):
        self.assertEqual(tulo(4,5),20)



if __name__=='__main__':
    unittest.main()