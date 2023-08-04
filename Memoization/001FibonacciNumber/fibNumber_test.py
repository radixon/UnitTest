import unittest
import fibonacciNumber
import fibNumber_cases

class TestFibNumber(unittest.TestCase):
    def test_fibNumber(self):
        # Test Cases can be found in fibNumber_cases.py
        case = fibonacciNumber.Solution()
        for i in range(len(fibNumber_cases.n)):
            self.assertEqual(case.fib(fibNumber_cases.n[i]),fibNumber_cases.res[i])
        

if __name__ == '__main__':
    unittest.main()