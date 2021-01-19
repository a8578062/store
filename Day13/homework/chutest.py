import unittest
from homework.calc import Calc
class TestDevide(unittest.TestCase):
    def testDevide1(self):
        c = Calc()
        a = 12
        b = 6
        s = 2
        sum = c.chu(a, b)
        self.assertEqual(s, sum)

    def testDevide2(self):
        c = Calc()
        a = 6
        b = 12
        s = 0.5
        sum = c.chu(a, b)
        self.assertEqual(s, sum)

    def testDevide3(self):
        c = Calc()
        a = 6
        b = -12
        s = -0.5
        sum = c.chu(a, b)
        self.assertEqual(s, sum)

    def testDevide4(self):
        c = Calc()
        a = -12
        b = 6
        s = -2
        sum = c.chu(a, b)
        self.assertEqual(s, sum)



