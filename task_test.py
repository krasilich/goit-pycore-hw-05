import unittest

from task1 import caching_fibonacci
from task2 import sum_profit, generator_numbers


class TestTask1(unittest.TestCase):
    def test_negative_input(self):
        self.assertEqual(caching_fibonacci()(-1), 0)

    def test_zero_input(self):
        self.assertEqual(caching_fibonacci()(0), 0)

    def test_positive_input(self):
        self.assertEqual(caching_fibonacci()(10), 55)


class TestTask2(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(sum_profit("", generator_numbers), 0)

    def test_no_numbers(self):
        self.assertEqual(sum_profit("test text", generator_numbers), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_profit("test -1 text", generator_numbers), -1)

    def test_empty_words(self):
        self.assertEqual(sum_profit("test  text  1", generator_numbers), 1)

    def test_valid_input(self):
        text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, "
                "доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
        self.assertEqual(sum_profit(text, generator_numbers), 1351.46)


if __name__ == '__main__':
    unittest.main()
