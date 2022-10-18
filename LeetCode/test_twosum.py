import unittest
import twosum

class TestProblem1(unittest.TestCase):
    def test_multiples_of_3_5(self):
        self.assertEqual(twosum.twoSum([2,7,11,15], 9),[0,1])
        self.assertEqual(twosum.twoSum([3,2,4], 6),[1,2])
        self.assertEqual(twosum.twoSum([3,3], 6),[0,1])


if __name__ == '__main__':
    unittest.main()