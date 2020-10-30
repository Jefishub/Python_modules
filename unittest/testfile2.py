import unittest
import newfile2

class SimpleTest(unittest.TestCase):
    def test_add(self):
        for i in range(10):
            self.assertEqual(newfile2.add(i,4),4+i)

    def test_multiply(self):
        for i in range(10):
            self.assertNotEqual(newfile2.multiply(i+1,5),0)


if __name__=='__main__':
    unittest.main()