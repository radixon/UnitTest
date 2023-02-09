import unittest
import productofarray
import productofarray_arr

class TestProductOfArray(unittest.TestCase):
    def test_productExceptSelf(self):
        # Provided Examples
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test1),[24,12,8,6])
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test2),[0,0,9,0,0])

        # Edge case: include one 0 at the beginning of the array
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test3),productofarray_arr.result3)

        # Edge case: include one 0 at the end of the array
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test4),productofarray_arr.result4)

        # Edge case: array of length 1500 tests O(n)
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test5),productofarray_arr.result5)

        # Edge case: array of length 3000 tests O(n)
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test6),productofarray_arr.result6)

        # Edge case: array of length 5000 with 0 appearing multiple times tests O(n)
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test7),productofarray_arr.result7)

        # General case: array of length 10 excluding 0 from the array
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test8),productofarray_arr.result8)

        # General case: array of length 15 excluding 0 from the array
        self.assertEqual(productofarray.productExceptSelf(productofarray_arr.test9),productofarray_arr.result9)


if __name__ == '__main__':
    unittest.main()
