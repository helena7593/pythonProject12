import unittest
from math import *

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(8))  # 7 is a prime number
        self.assertTrue(is_prime(13))  # 13 is a prime number

    def test_non_prime_number(self):
        self.assertFalse(is_prime(4))  # 4 is not a prime number
        self.assertFalse(is_prime(9))  # 9 is not a prime number

    def test_edge_cases(self):
        self.assertFalse(is_prime(0))  # 0 is not a prime number
        self.assertFalse(is_prime(1))  # 1 is not a prime number

    def test_large_prime_number(self):
        self.assertTrue(is_prime(101))  # 101 is a prime number

    def test_large_non_prime_number(self):
        self.assertFalse(is_prime(100))  # 100 is not a prime number

if __name__ == "__main__":
    unittest.main()