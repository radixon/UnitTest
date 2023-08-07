import unittest
import minCostClimbingStairs
import minCostClimbingStairs_cases

class TestClimbStairs(unittest.TestCase):
    def test_minCostClimbingStairs(self):
        # Test Cases can be found in minCostClimbingStairs_cases.py
        case = minCostClimbingStairs.Solution()
        for i in range(len(minCostClimbingStairs_cases.res)):
            self.assertEqual(case.minCostClimbingStairs(minCostClimbingStairs_cases.cost[i]),minCostClimbingStairs_cases.res[i])
        

if __name__ == '__main__':
    unittest.main()