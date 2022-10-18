import unittest
import fizzbuzz

class TestProblem1(unittest.TestCase):
    def test_fizzbuzz(self):
        # Edge case of zero
        self.assertEqual(fizzbuzz.fizzbuzz(0),0)

        # Edge case of 15
        self.assertEqual(fizzbuzz.fizzbuzz(15),"FizzBuzz")

        # Edge case of -3
        self.assertEqual(fizzbuzz.fizzbuzz(-3),"Fizz")

        # Edge case of -5
        self.assertEqual(fizzbuzz.fizzbuzz(-5),"Buzz")

        # Multiples of 3 and not 5
        self.assertEqual(fizzbuzz.fizzbuzz(3),"Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(33),"Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(81),"Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(168),"Fizz")
        self.assertEqual(fizzbuzz.fizzbuzz(2223),"Fizz")

        # Multiples of 5 and not 3
        self.assertEqual(fizzbuzz.fizzbuzz(5),"Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(10),"Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-575),"Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-665),"Buzz")
        self.assertEqual(fizzbuzz.fizzbuzz(2215),"Buzz")

        # Multiples of 3 and 5
        self.assertEqual(fizzbuzz.fizzbuzz(-15),"FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(30),"FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(375),"FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(-660),"FizzBuzz")
        self.assertEqual(fizzbuzz.fizzbuzz(2220),"FizzBuzz")


if __name__ == '__main__':
    unittest.main()