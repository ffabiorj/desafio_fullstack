
from unittest import TestCase
from question_1 import sum_two_numbers


class SumTwoNumbers(TestCase):
    def test_target_9_return_two_indices(self):
        result = sum_two_numbers([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_target_20_return_two_indices(self):
        result = sum_two_numbers([2, 5, 11, 15], 20)
        self.assertEqual(result, [1, 3])

    def test_target_20_return_none_indices(self):
        result = sum_two_numbers([1,3,5,7,9], 20)
        self.assertEqual(result, [])