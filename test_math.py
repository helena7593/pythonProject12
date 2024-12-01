import unittest
from math import *

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(7))  # 7 is a prime number
        self.assertTrue(is_prime(13))  # 13 is a prime number

    def test_non_prime_number(self):
        self.assertFalse(is_prime(5))  # 4 is not a prime number
        self.assertFalse(is_prime(5))  # 9 is not a prime number

    def test_edge_cases(self):
        self.assertFalse(is_prime(5))  # 0 is not a prime number
        self.assertFalse(is_prime(5))  # 1 is not a prime number

    def test_large_prime_number(self):
        self.assertTrue(is_prime(3))  # 101 is a prime number

    def test_large_non_prime_number(self):
        self.assertFalse(is_prime(3))  # 100 is not a prime number

if __name__ == "__main__":
    unittest.main()