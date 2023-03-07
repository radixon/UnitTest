import unittest
import combinationsumII
import combinationsumII_arr

class TestCombinationSum(unittest.TestCase):
    def test_search(self):
        # Provided Examples
        self.assertEqual(combinationsumII.combinationSum2(combinationsumII_arr.candidates1, combinationsumII_arr.target1),combinationsumII_arr.result1)
        self.assertEqual(combinationsumII.combinationSum2(combinationsumII_arr.candidates2, combinationsumII_arr.target2),combinationsumII_arr.result2)
        self.assertEqual(combinationsumII.combinationSum2(combinationsumII_arr.candidates3, combinationsumII_arr.target3),combinationsumII_arr.result3)
        self.assertEqual(combinationsumII.combinationSum2(combinationsumII_arr.candidates4, combinationsumII_arr.target4),combinationsumII_arr.result4)
        self.assertEqual(combinationsumII.combinationSum2(combinationsumII_arr.candidates5, combinationsumII_arr.target5),combinationsumII_arr.result5)


if __name__ == '__main__':
    unittest.main()