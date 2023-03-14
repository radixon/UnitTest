import unittest
import trappingrainwater
import trappingrainwater_arr

class TestTrappingRainWater(unittest.TestCase):
    def test_search(self):
        # Examples
        self.assertEqual(trappingrainwater.trap(trappingrainwater_arr.height1),trappingrainwater_arr.result1)
        self.assertEqual(trappingrainwater.trap(trappingrainwater_arr.height2),trappingrainwater_arr.result2)
        self.assertEqual(trappingrainwater.trap(trappingrainwater_arr.height3),trappingrainwater_arr.result3)
        self.assertEqual(trappingrainwater.trap(trappingrainwater_arr.height4),trappingrainwater_arr.result4)
        self.assertEqual(trappingrainwater.trap(trappingrainwater_arr.height5),trappingrainwater_arr.result5)
        self.assertEqual(trappingrainwater.trap(trappingrainwater_arr.height6),trappingrainwater_arr.result6)
        self.assertEqual(trappingrainwater.trap(trappingrainwater_arr.height7),trappingrainwater_arr.result7)


if __name__ == '__main__':
    unittest.main()