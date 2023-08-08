class Solution():
    """
    Time Complexity: O(n)
    The algorithm will loop n times

    Space Complexity: O(1)
    Constant extra space is used on res, curr, and prev variables.
    """
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
