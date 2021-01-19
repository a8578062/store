import unittest
from homework.calc import Calc
class TestIncre(unittest.TestCase):
    def testIncre1(self):
        c = Calc()
        a = 5
        b = 6
        s = -1
        sum = c.jian(a, b)
        self.assertEqual(s, sum)

    def testIncre2(self):
        c = Calc()
        a = 5
        b = -6
        s = 11
        sum = c.jian(a, b)
        self.assertEqual(s, sum)

    def testIncre3(self):
        c = Calc()
        a = -5
        b = 6
        s = -11
        sum = c.jian(a, b)
        self.assertEqual(s, sum)

    def testIncre4(self):
        c = Calc()
        a = -5
        b = -6
        s = 1
        sum = c.jian(a, b)
        self.assertEqual(s, sum)


    def testIncre5(self):
        c = Calc()
        a = 0
        b = -6
        s = 6
        sum = c.jian(a, b)
        self.assertEqual(s, sum)

    def testIncre6(self):
        c = Calc()
        a = -5
        b = 0
        s = -5
        sum = c.jian(a, b)
        self.assertEqual(s, sum)

