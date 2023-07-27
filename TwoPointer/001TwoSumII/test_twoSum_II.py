import unittest
import twoSum_II
import twoSum_II_arr

class TestTwoSum(unittest.TestCase):
    def test_twoSum(self):
        # Examples in twoSum_II_arr.py file
        for i in range(len(twoSum_II_arr.test)):
            self.assertEqual(twoSum_II.twoSum(twoSum_II_arr.test[i], twoSum_II_arr.target[i]),twoSum_II_arr.result[i])
        

if __name__ == '__main__':
    unittest.main()
