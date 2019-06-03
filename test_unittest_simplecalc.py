from simple_calc import *
import unittest

class CalcTests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        # Syntax: assertEqual(#test value, #expected outcome)
        self.assertEqual(self.calc.add(2,4),6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,4),-2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,4),8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2,4),0.5)
