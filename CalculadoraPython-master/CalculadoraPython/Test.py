from unittest import TestCase
import unittest
from main import factorial, trignometrics, power

# -*- coding: UTF-8 -*-
class Test(TestCase):
    def test_factorial(self):
        self.assertEqual(factorial('3!'), 6)
        self.assertEqual(factorial('10!'), 3628800)
        self.assertEqual(factorial('-10!'))  # Deve lançar exceção
        self.fail()

    def test_trignometrics(self):
        self.assertEqual(trignometrics('cos 0'), 1.0)
        self.assertEqual(trignometrics('sen 0'), 0.0)
        self.assertEqual(trignometrics('tan 0'), 0.0)
        self.fail()

    def test_power(self):
        self.assertEqual(power('^ 5 3'), 125.0)
        self.assertEqual(power('^ 5 infinity'), 'inf')
        self.fail()

if __name__ == '__main__':
    unittest.main()