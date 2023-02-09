import unittest
import containsduplicate
import containsduplicate_arr

class TestContainsDuplicate(unittest.TestCase):
    def test_containsDuplicate(self):
        # Provided Examples
        self.assertEqual(containsduplicate.containsDuplicate([1,2,3,1]),True)
        self.assertEqual(containsduplicate.containsDuplicate([1,2,3,4]),False)
        self.assertEqual(containsduplicate.containsDuplicate([1,1,1,3,3,4,3,2,4,2]),True)

        # Arrays produced using random.randint()
        self.assertEqual(containsduplicate.containsDuplicate(containsduplicate_arr.test1),False)
        self.assertEqual(containsduplicate.containsDuplicate(containsduplicate_arr.test2),False)

        # Edge case with array of length 2 without a duplicate
        self.assertEqual(containsduplicate.containsDuplicate(containsduplicate_arr.test3),False)

        # Edge case with array of length 2 with a duplicate
        self.assertEqual(containsduplicate.containsDuplicate(containsduplicate_arr.test4),True)

        # Edge case with empty array
        self.assertEqual(containsduplicate.containsDuplicate(containsduplicate_arr.test5),False)

        # Edge case with array of length 1
        self.assertEqual(containsduplicate.containsDuplicate(containsduplicate_arr.test6),False)          



if __name__ == '__main__':
    unittest.main()
