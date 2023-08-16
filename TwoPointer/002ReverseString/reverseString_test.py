import unittest
import reverseString
import reverseString_cases

class TestReverseString(unittest.TestCase):
    def test_reverseString(self):
        # Test Cases can be found in reverseString_cases.py
        s = reverseString_cases.s
        res = reverseString_cases.res
        case = reverseString.Solution()
        for i in range(len(s)):
            try: 
                self.assertEqual(case.reverseString(s[i]),res[i])
            except AssertionError:
                print("Failed Case")
                print('Case: ', i, '\t' ,'s: ', s[i],'\t','Calculated Result: ',case.reverseString(s[i]),'\n')
        

if __name__ == '__main__':
    unittest.main()