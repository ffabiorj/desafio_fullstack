from unittest import TestCase
from question_3 import max_profit


class MaxProfitTest(TestCase):
    def test_return_of_profit_5(self):
        result = max_profit([1,4,3,6,2,2])
        self.assertEqual(result, 5)
    
    def test_return_of_profit_10(self):
        result = max_profit([2,4,3,6,2,2,14])
        self.assertEqual(result, 12)

    def test_return_of_profit_0(self):
        result = max_profit([7,4,3,1,1,1])
        self.assertEqual(result, 0)
