import unittest
import palindromeNumber

class TestPalindromeNumber(unittest.TestCase):
    def test_palindromeNumber(self):
        # Provided Examples
        self.assertEqual(palindromeNumber.isPalindrome(0),True)
        self.assertEqual(palindromeNumber.isPalindrome(121),True)
        self.assertEqual(palindromeNumber.isPalindrome(10),False)
        self.assertEqual(palindromeNumber.isPalindrome(-121),False)
        self.assertEqual(palindromeNumber.isPalindrome(101),True)
        self.assertEqual(palindromeNumber.isPalindrome(1001),True)
        self.assertEqual(palindromeNumber.isPalindrome(10001),True) 
        self.assertEqual(palindromeNumber.isPalindrome(100001),True)
        self.assertEqual(palindromeNumber.isPalindrome(1000001),True)
        self.assertEqual(palindromeNumber.isPalindrome(10000001),True)
        self.assertEqual(palindromeNumber.isPalindrome(151121),False)
        self.assertEqual(palindromeNumber.isPalindrome(15151),True)
        self.assertEqual(palindromeNumber.isPalindrome(151151),True)
                     
if __name__ == '__main__':
    unittest.main()