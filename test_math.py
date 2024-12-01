import unittest
from math import *

def test_is_prime_with_prime_number():
    assert is_prime(5) == True

def test_is_prime_with_non_prime_number():
    assert is_prime(4) == False

def test_is_prime_with_negative_number():
    assert is_prime(-1) == False

def test_is_prime_with_zero():
    assert is_prime(0) == False

def test_is_prime_with_one():
    assert is_prime(1) == False

if __name__ == "__main__":
    unittest.main()