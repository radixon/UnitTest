import unittest
import combinationsumIII
import combinationsumIII_arr

class TestCombinationSum(unittest.TestCase):
    def test_search(self):
        # Provided Examples
        self.assertEqual(combinationsumIII.combinationSum3(combinationsumIII_arr.k1, combinationsumIII_arr.n1),combinationsumIII_arr.result1)
        self.assertEqual(combinationsumIII.combinationSum3(combinationsumIII_arr.k2, combinationsumIII_arr.n2),combinationsumIII_arr.result2)
        self.assertEqual(combinationsumIII.combinationSum3(combinationsumIII_arr.k3, combinationsumIII_arr.n3),combinationsumIII_arr.result3)
        self.assertEqual(combinationsumIII.combinationSum3(combinationsumIII_arr.k4, combinationsumIII_arr.n4),combinationsumIII_arr.result4)
        self.assertEqual(combinationsumIII.combinationSum3(combinationsumIII_arr.k5, combinationsumIII_arr.n5),combinationsumIII_arr.result5)


if __name__ == '__main__':
    unittest.main()