import unittest
import calculator
class Calctest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2,5),7)
        self.assertEqual(calculator.add(1,5),6)
        self.assertEqual(calculator.add(3,5),8)
        self.assertEqual(calculator.add(2,0),2)
