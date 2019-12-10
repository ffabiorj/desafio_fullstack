from unittest import TestCase
from question_2 import try_correct_order


class TryCorrectOrderTest(TestCase):
    def test_return_yes_with_length_string_12(self):
        result = try_correct_order('{{[[(())]]}}')
        self.assertEqual(result, 'SIM')

    def test_return_yes_with_len_string_4(self):
        result = try_correct_order('({})')
        self.assertEqual(result, 'SIM')

    def test_return_no_with_len_string_0(self):
        result = try_correct_order('')
        self.assertEqual(result, 'NÃO')

    def test_return_no_with_len_string_6(self):
        result = try_correct_order('[{}{}]')
        self.assertEqual(result, 'NÃO')
