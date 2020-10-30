import unittest
import newfile1

class SimpleTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(newfile1.add(5,4),9)

    def test_add2(self):
        self.assertEqual(newfile1.tulo(4,5),20)


if __name__=='__main__':
    unittest.main()