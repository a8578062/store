import unittest
from homework.calc import Calc
class TestMulti(unittest.TestCase):
    def testMulti1(self):
        c = Calc()
        a = 5
        b = 6
        s = 30
        sum = c.cheng(a, b)
        self.assertEqual(s, sum)

    def testMulti2(self):
        c = Calc()
        a = 5
        b = -6
        s = -30
        sum = c.cheng(a, b)
        self.assertEqual(s, sum)

    def testMulti3(self):
        c = Calc()
        a = -5
        b = 6
        s = -30
        sum = c.cheng(a, b)
        self.assertEqual(s, sum)

    def testMulti4(self):
        c = Calc()
        a = -5
        b = -6
        s = 30
        sum = c.cheng(a, b)
        self.assertEqual(s, sum)


    def testMulti5(self):
        c = Calc()
        a = 0
        b = -6
        s = 0
        sum = c.cheng(a, b)
        self.assertEqual(s, sum)

    def testMulti6(self):
        c = Calc()
        a = -5
        b = 0
        s = 0
        sum = c.cheng(a, b)
        self.assertEqual(s, sum)

