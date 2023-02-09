import unittest
import minimumInRotatedII
import minimumInRotatedII_arr

class TestMinimumInRotatedII(unittest.TestCase):
    def test_findMin(self):
        # Provided Examples
        self.assertEqual(minimumInRotatedII.findMin(minimumInRotatedII_arr.test1),minimumInRotatedII_arr.result1)
        self.assertEqual(minimumInRotatedII.findMin(minimumInRotatedII_arr.test2),minimumInRotatedII_arr.result2)
        self.assertEqual(minimumInRotatedII.findMin(minimumInRotatedII_arr.test3),minimumInRotatedII_arr.result3)

        # General Cases
        self.assertEqual(minimumInRotatedII.findMin(minimumInRotatedII_arr.test4),minimumInRotatedII_arr.result4)
        self.assertEqual(minimumInRotatedII.findMin(minimumInRotatedII_arr.test5),minimumInRotatedII_arr.result5)
        self.assertEqual(minimumInRotatedII.findMin(minimumInRotatedII_arr.test6),minimumInRotatedII_arr.result6)

        

if __name__ == '__main__':
    unittest.main()