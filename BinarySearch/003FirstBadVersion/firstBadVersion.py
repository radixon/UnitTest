class Solution:
    def __init__(self,bad=0):
        self.bad = bad
    
    def firstBadVersion(self,n: int):
        low, high = 1, n
        while low < high:
            mid = low + (high-low)//2
            if self.isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low
    
    def isBadVersion(self, x: int):
        if x >= self.bad:
            return True
        else:
            return False  

if __name__ == '__main__':
    res = Solution(4)
    print(res.firstBadVersion(5))

    res = Solution(1)
    print(res.firstBadVersion(1))

    res = Solution(2)
    print(res.firstBadVersion(2))

    res = Solution(10)
    print(res.firstBadVersion(2**31 - 1))