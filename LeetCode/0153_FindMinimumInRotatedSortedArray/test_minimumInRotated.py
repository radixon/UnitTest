import unittest
import minimumInRotated
import minimumInRotated_arr

class TestMinimumInRotated(unittest.TestCase):
    def test_findMin(self):
        # Provided Examples
        self.assertEqual(minimumInRotated.findMin(minimumInRotated_arr.test1),minimumInRotated_arr.result1)
        self.assertEqual(minimumInRotated.findMin(minimumInRotated_arr.test2),minimumInRotated_arr.result2)
        self.assertEqual(minimumInRotated.findMin(minimumInRotated_arr.test3),minimumInRotated_arr.result3)

        # General Cases
        self.assertEqual(minimumInRotated.findMin(minimumInRotated_arr.test4),minimumInRotated_arr.result4)
        self.assertEqual(minimumInRotated.findMin(minimumInRotated_arr.test5),minimumInRotated_arr.result5)

        

if __name__ == '__main__':
    unittest.main()
