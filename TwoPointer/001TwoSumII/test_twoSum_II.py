import unittest
import twoSum_II
import twoSum_II_arr

class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        # Provided Examples
        self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test1, twoSum_II_arr.target1),twoSum_II_arr.result1)
        self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test2, twoSum_II_arr.target2),twoSum_II_arr.result2)
        self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test3, twoSum_II_arr.target3),twoSum_II_arr.result3)

        # General Case
        self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test4, twoSum_II_arr.target4),twoSum_II_arr.result4)

        # Edge Case last two indexes equals target
        self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test5, twoSum_II_arr.target5),twoSum_II_arr.result5)

        # Edge Case with negative number
        self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test6, twoSum_II_arr.target6),twoSum_II_arr.result6)

        # Edge Case two negative numbers equals the target value
        self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test7, twoSum_II_arr.target7),twoSum_II_arr.result7)


if __name__ == '__main__':
    unittest.main()
