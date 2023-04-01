import unittest
import jumpgame
import jumpgame_arr

class TestJumpGame(unittest.TestCase):
    def test_jumpgame(self):
        # Provided Examples
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums1),True)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums2),False)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums3),True)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums4),False)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums5),False)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums6),True)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums7),False) 
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums8),False)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums9),True)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums10),True)
        self.assertEqual(jumpgame.canJump(jumpgame_arr.nums11),False)
                     
if __name__ == '__main__':
    unittest.main()