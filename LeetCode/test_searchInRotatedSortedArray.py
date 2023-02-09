import unittest
import searchInRotatedSortedArray
import searchInRotatedSortedArray_arr

class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_search(self):
        # Provided Examples
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test1, searchInRotatedSortedArray_arr.target1),searchInRotatedSortedArray_arr.result1)
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test2, searchInRotatedSortedArray_arr.target2),searchInRotatedSortedArray_arr.result2)
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test3, searchInRotatedSortedArray_arr.target3),searchInRotatedSortedArray_arr.result3)

        # General Case
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test4, searchInRotatedSortedArray_arr.target4),searchInRotatedSortedArray_arr.result4)
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test5, searchInRotatedSortedArray_arr.target5),searchInRotatedSortedArray_arr.result5)
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test6, searchInRotatedSortedArray_arr.target6),searchInRotatedSortedArray_arr.result6)
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test7, searchInRotatedSortedArray_arr.target7),searchInRotatedSortedArray_arr.result7)
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test8, searchInRotatedSortedArray_arr.target8),searchInRotatedSortedArray_arr.result8)
        self.assertEqual(searchInRotatedSortedArray.search(searchInRotatedSortedArray_arr.test9, searchInRotatedSortedArray_arr.target9),searchInRotatedSortedArray_arr.result9)


if __name__ == '__main__':
    unittest.main()