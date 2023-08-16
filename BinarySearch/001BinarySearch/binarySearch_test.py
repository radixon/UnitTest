import unittest
import binarySearch
import binarySearch_cases

class TestBinarySearch(unittest.TestCase):
    def test_binarySearch(self):
        # Test Cases can be found in binarySearch_cases.py
        nums = binarySearch_cases.nums
        target = binarySearch_cases.target
        res = binarySearch_cases.res
        for i in range(len(target)):
            case = binarySearch.Solution()
            try: 
                self.assertEqual(case.search(nums[i],target[i]),res[i])
            except AssertionError:
                print("Failed Case")
                print('Case: ',i,'\t','nums: ', nums[i],'\t','target: ',target[i],'\t','Result: ',res[i],'\n')
        

if __name__ == '__main__':
    unittest.main()