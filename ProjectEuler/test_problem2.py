import unittest
import problem2

class TestProblem1(unittest.TestCase):
    def test_fibonacci(self):
        # Provided Example
        self.assertEqual(problem2.fibonacci(89),44)

        # Edge case of fibonacci of length 0
        self.assertEqual(problem2.fibonacci(0),0)

        # Edge case of fibonacci of length 1
        self.assertEqual(problem2.fibonacci(1),0)

        # Edge case of fibonacci of length 2
        self.assertEqual(problem2.fibonacci(2),2)

        # Edge case of fibonacci of length 3
        self.assertEqual(problem2.fibonacci(3),2)

        # Examples
        self.assertEqual(problem2.fibonacci(5),2)
        self.assertEqual(problem2.fibonacci(10),10)
        self.assertEqual(problem2.fibonacci(500),188)
        self.assertEqual(problem2.fibonacci(1250),798)
        self.assertEqual(problem2.fibonacci(10000),3382)
        self.assertEqual(problem2.fibonacci(100000),60696)

        # Question asked to solve
        self.assertEqual(problem2.fibonacci(4000000),4613732)


if __name__ == '__main__':
    unittest.main()