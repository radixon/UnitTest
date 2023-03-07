import unittest
import combinationsum
import combinationsum_arr

class TestCombinationSum(unittest.TestCase):
    def test_search(self):
        # Provided Examples
        self.assertEqual(combinationsum.combinationSum(combinationsum_arr.candidates1, combinationsum_arr.target1),combinationsum_arr.result1)
        self.assertEqual(combinationsum.combinationSum(combinationsum_arr.candidates2, combinationsum_arr.target2),combinationsum_arr.result2)
        self.assertEqual(combinationsum.combinationSum(combinationsum_arr.candidates3, combinationsum_arr.target3),combinationsum_arr.result3)
        self.assertEqual(combinationsum.combinationSum(combinationsum_arr.candidates4, combinationsum_arr.target4),combinationsum_arr.result4)
        self.assertEqual(combinationsum.combinationSum(combinationsum_arr.candidates5, combinationsum_arr.target5),combinationsum_arr.result5)


if __name__ == '__main__':
    unittest.main()