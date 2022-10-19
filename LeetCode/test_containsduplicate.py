import unittest
import containsduplicate

class TestContainsDuplicate(unittest,TestCase):
    def test_containsDuplicate(self):
        # Provided Examples
        self.assertEqual(containsduplicate.containsDuplicate([1,2,3,1]),True)
        self.assertEqual(containsduplicate.containsDuplicate([1,2,3,4]),False)
        self.assertEqual(containsduplicate.containsDuplicate([1,1,1,3,3,4,3,2,4,2]),True)


if __name__ == '__main__':
    unittest.main()