import unittest
import problem1

class TestProblem1(unittest.TestCase):
    def test_multiples_of_3_5(self):
        self.assertEqual(problem1.multiples_of_3_5(10),23)
        self.assertEqual(problem1.multiples_of_3_5(3),0)
        self.assertEqual(problem1.multiples_of_3_5(5),3)
        self.assertEqual(problem1.multiples_of_3_5(0),0)
        self.assertEqual(problem1.multiples_of_3_5(1000),233168)
        self.assertEqual(problem1.multiples_of_3_5(100),2318)

        self.assertEqual(problem1.multiples_of_3_5(3,-3),-3)
        self.assertEqual(problem1.multiples_of_3_5(4,-3),0)
        self.assertEqual(problem1.multiples_of_3_5(1000,-100),230750)


if __name__ == '__main__':
    unittest.main()