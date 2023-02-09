import unittest
import containerwithmostwater
import containerwithmostwater_arr

class TestContainerWithMostWater(unittest.TestCase):
    def test_maxArea(self):
        # Provided Examples
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test1),containerwithmostwater_arr.result1)
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test2),containerwithmostwater_arr.result2)
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test3),containerwithmostwater_arr.result3)

        # General Cases
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test4),containerwithmostwater_arr.result4)
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test5),containerwithmostwater_arr.result5)
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test6),containerwithmostwater_arr.result6)
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test7),containerwithmostwater_arr.result7)
        self.assertEqual(containerwithmostwater.maxArea(containerwithmostwater_arr.test8),containerwithmostwater_arr.result8)

        

if __name__ == '__main__':
    unittest.main()