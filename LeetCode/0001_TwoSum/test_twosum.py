import unittest
import twosum
import twosum_arr

class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        # Provided Examples
        self.assertEqual(twosum.twoSum([2,7,11,15], 9),[0,1])
        self.assertEqual(twosum.twoSum([3,2,4], 6),[1,2])
        self.assertEqual(twosum.twoSum([3,3], 6),[0,1])

        # Edge Case with 0 as part of the sum
        self.assertEqual(twosum.twoSum(twosum_arr.edge0, 13),[0,3])

        # Edge Case with beginning and end of array as part of the sum
        self.assertEqual(twosum.twoSum(twosum_arr.edge1, 265),[6,8])

        # Edge Case with negative number
        self.assertEqual(twosum.twoSum(twosum_arr.edge2, 2),[2,5])

        # Edge Case of target value in the array not being in the answer
        self.assertEqual(twosum.twoSum(twosum_arr.edge3, 216),[3,7])

        # Edge Case of two answers available
        self.assertEqual(twosum.twoSum(twosum_arr.edge4, 340),[4,5])

        # Random Generated Arrays
        self.assertEqual(twosum.twoSum(twosum_arr.num0, 132),[18,28])
        self.assertEqual(twosum.twoSum(twosum_arr.num1, 325),[32,39])
        self.assertEqual(twosum.twoSum(twosum_arr.num2, 1218),[4,29])
        self.assertEqual(twosum.twoSum(twosum_arr.num3, 6651),[10,73])
        self.assertEqual(twosum.twoSum(twosum_arr.num4, 103269),[1,9])


if __name__ == '__main__':
    unittest.main()
