import unittest
import maximumsubarray
import maximumsubarray_arr

class TestProductOfArray(unittest.TestCase):
    def test_maxSubArray(self):
        # Provided Examples
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test1),6)
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test2),1)
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test3),23)

        # Edge Case: All positive numbers ascending order
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test4),maximumsubarray_arr.result4)

        # Edge Case: All positive numbers descending order
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test5),maximumsubarray_arr.result5)

        # Edge Case: All negative numbers ascending order
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test6),maximumsubarray_arr.result6)

        # Edge Case: All negative numbers descending order
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test7),maximumsubarray_arr.result7)

        # General Cases
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test8),maximumsubarray_arr.result8)
        self.assertEqual(maximumsubarray.maxSubArray(maximumsubarray_arr.test9),maximumsubarray_arr.result10)

        

if __name__ == '__main__':
    unittest.main()