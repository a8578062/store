import unittest
from homework.calc import Calc


class TestAdd(unittest.TestCase):
    def testAdd1(self):
        c = Calc()
        a = 5
        b = 6
        s = 11
        sum = c.jia(a, b)
        self.assertEqual(s, sum)

    def testAdd2(self):
        c = Calc()
        a = 5
        b = -6
        s = -1
        sum = c.jia(a, b)
        self.assertEqual(s, sum)

    def testAdd3(self):
        c = Calc()
        a = -5
        b = 6
        s = 1
        sum = c.jia(a, b)
        self.assertEqual(s, sum)

    def testAdd4(self):
        c = Calc()
        a = -5
        b = -6
        s = -11
        sum = c.jia(a, b)
        self.assertEqual(s, sum)


    def testAdd5(self):
        c = Calc()
        a = 0
        b = -6
        s = -6
        sum = c.jia(a, b)
        self.assertEqual(s, sum)

    def testAdd6(self):
        c = Calc()
        a = -5
        b = 0
        s = -5
        sum = c.jia(a, b)
        self.assertEqual(s, sum)

