class Solution:
    def __init__(self,pick = 0):
        self.pick = pick

    def guessNumber(self, n: int) -> int:
        """
        Time Complexity:    O(log n)
        Space Complexity:   O(1)
        """
        low, high = 1, n
        while low < high:
            mid = high - (high - low)//2
            res = self.guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def guess(self,x: int):
        if x > self.pick: return -1
        if x < self.pick: return 1
        else: return 0



if __name__ == '__main__':
    res = Solution(6)
    print(res.guessNumber(10))

    res = Solution(1)
    print(res.guessNumber(1))

    res = Solution(2)
    print(res.guessNumber(1))

    res = Solution(2**31 - 2)
    print(res.guessNumber(2**31 - 1))
