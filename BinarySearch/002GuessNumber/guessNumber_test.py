import unittest
import guessNumber
import guessNumber_cases

class TestGuessNumber(unittest.TestCase):
    def test_guessNumber(self):
        # Test Cases can be found in guessNumber_cases.py
        n = guessNumber_cases.n
        num = guessNumber_cases.num
        for i in range(len(n)):
            case = guessNumber.Solution(num[i])
            try: 
                self.assertEqual(case.guessNumber(n[i]),num[i])
            except AssertionError:
                print("Failed Case")
                print('Case: ',i,'\t','n: ', n[i],'\t','num: ',num[i],'\n')
        

if __name__ == '__main__':
    unittest.main()