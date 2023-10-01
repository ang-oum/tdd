import unittest

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True



class PrimeNumberTestCase(unittest.TestCase):       
    def test_prime_numbers(self):
        prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        #prime_numbers = [2, 3, 4, 8, 11, 13, 17, 19, 23, 30, 31]
        print("Prime numbers:",prime_numbers)
        for number in prime_numbers:
            self.assertTrue(is_prime(number), f"{number} is not recognized as a prime number")

    def test_non_prime_numbers(self):
        non_prime_numbers = [4, 6, 8, 10, 12, 14, 16, 18, 20]
        #non_prime_numbers = [4, 6, 8, 9, 11, 12, 14, 17, 16, 18, 20]
        print("Non prime numbers:",non_prime_numbers)

        for number in non_prime_numbers:
            self.assertFalse(is_prime(number), f"{number} is incorrectly recognized as a prime number")


if __name__ == '__main__':
    unittest.main()