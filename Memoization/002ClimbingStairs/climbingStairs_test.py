import unittest
import climbingStairs
import climbingStairs_cases

class TestClimbStairs(unittest.TestCase):
    def test_climbStair(self):
        # Test Cases can be found in climbingStairs_cases.py
        case = climbingStairs.Solution()
        for i in range(len(climbingStairs_cases.n)):
            self.assertEqual(case.climbStairs(climbingStairs_cases.n[i]),climbingStairs_cases.res[i])
        

if __name__ == '__main__':
    unittest.main()