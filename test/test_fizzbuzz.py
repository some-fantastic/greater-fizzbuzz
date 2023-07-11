import unittest
from src import fizzbuzz


class TestRunFizzbuzz(unittest.TestCase):
    def test_run_fizzbuzz_with_fizzbuzz_number(self):
        self.assertEqual(fizzbuzz.run_fizzbuzz(15), "fizzbuzz")

    def test_run_fizzbuzz_with_fizz_number(self):
        self.assertEqual(fizzbuzz.run_fizzbuzz(9), "fizz")

    def test_run_fizzbuzz_with_buzz_number(self):
        self.assertEqual(fizzbuzz.run_fizzbuzz(10), "buzz")

    def test_run_fizzbuzz_with_non_fizzbuzz_number(self):
        self.assertEqual(fizzbuzz.run_fizzbuzz(7), "no fizzbuzz for you!")


class TestIsNumber(unittest.TestCase):
    def test_is_number_with_valid_input(self):
        self.assertTrue(fizzbuzz.is_number("123"))
        self.assertTrue(fizzbuzz.is_number("-456"))
        self.assertTrue(fizzbuzz.is_number("0"))

    def test_is_number_with_invalid_input(self):
        self.assertFalse(fizzbuzz.is_number("abc"))
        self.assertFalse(fizzbuzz.is_number("1.23"))
        self.assertFalse(fizzbuzz.is_number("1,000"))


if __name__ == "__main__":
    unittest.main()
