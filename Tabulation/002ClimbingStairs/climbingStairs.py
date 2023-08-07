class Solution():
    def climbStairs(self,n: int) -> int:
        res, curr = 1, 1
        for i in range(n):
            prev = res
            res = curr
            curr = prev + curr
        return res

if __name__ == "__main__":
    ans = Solution()
    for i in range(8):
        print(ans.climbStairs(i))