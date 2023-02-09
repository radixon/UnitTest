import unittest
import maximumproductsubarray
import maximumproductsubarray_arr

class TestProductOfArray(unittest.TestCase):
    def test_maxProduct(self):
        # Provided Examples
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test1),6)
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test2),0)

        # Edge Case: All positive numbers ascending order
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test3),maximumproductsubarray_arr.result3)

        # Edge Case: All positive numbers ascending order with zero at the beginning of the list
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test4),maximumproductsubarray_arr.result4)

        # Edge Case: All positive numbers ascending order with zero at the end of the list
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test5),maximumproductsubarray_arr.result5)

        # Edge Case: An even number of negative numbers
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test6),maximumproductsubarray_arr.result6)

        # Edge Case: An odd number of negative numbers with zero at the beginning of the list
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test7),maximumproductsubarray_arr.result7)
        
        # Edge Case: An odd number of negative numbers with zero at the end of the list
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test8),maximumproductsubarray_arr.result8)

        # Edge Case: An odd number of negative numbers with zero at the middle of the list
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test9),maximumproductsubarray_arr.result9)

        # Edge Case: An odd number of negative numbers with multiple zeros in the list
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test10),maximumproductsubarray_arr.result10)

        # Edge Case: All positive numbers ascending order with multiple zeros in the list
        self.assertEqual(maximumproductsubarray.maxProduct(maximumproductsubarray_arr.test11),maximumproductsubarray_arr.result11)

        

if __name__ == '__main__':
    unittest.main()
