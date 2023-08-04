class Solution():
    memo = {0:1,1:1}
    def climbStairs(self,n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

if __name__ == "__main__":
    res = Solution()
    for i in [0,1,2,3,5,8,9]:
        print(res.climbStairs(i))