import unittest
import threeSum
import threeSum_arr

class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        # Provided Examples
        self.assertEqual(threeSum.threeSum(threeSum_arr.test1),threeSum_arr.result1)
        self.assertEqual(threeSum.threeSum(threeSum_arr.test2),threeSum_arr.result2)
        self.assertEqual(threeSum.threeSum(threeSum_arr.test3),threeSum_arr.result3)

        # General Case
        self.assertEqual(threeSum.threeSum(threeSum_arr.test4),threeSum_arr.result4)

        # Edge Case last two indexes equals target
        self.assertEqual(threeSum.threeSum(threeSum_arr.test5),threeSum_arr.result5)

        # Edge Case with negative number
        self.assertEqual(threeSum.threeSum(threeSum_arr.test6),threeSum_arr.result6)

        # Edge Case two negative numbers equals the target value
        self.assertEqual(threeSum.threeSum(threeSum_arr.test7),threeSum_arr.result7)


if __name__ == '__main__':
    unittest.main()