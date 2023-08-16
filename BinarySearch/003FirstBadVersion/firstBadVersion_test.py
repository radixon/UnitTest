import unittest
import firstBadVersion
import firstBadVersion_cases

class TestFirstBadVersion(unittest.TestCase):
    def test_firstBadVersion(self):
        # Test Cases can be found in firstBadVersion_cases.py
        n = firstBadVersion_cases.n
        bad = firstBadVersion_cases.bad
        for i in range(len(n)):
            case = firstBadVersion.Solution(bad[i])
            try: 
                self.assertEqual(case.firstBadVersion(n[i]),bad[i])
            except AssertionError:
                print("Failed Case")
                print('Case: ', i, '\t', 'n: ', n[i],'\t','bad: ',bad[i],'\n')
        

if __name__ == '__main__':
    unittest.main()
