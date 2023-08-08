class Solution():
    """
    Time Complexity: O(n)
    The algorithm will loop n times.

    Space Complexity: O(1)
    Constant extra space is used for res, curr, and prev variables.
    """
    def fib(self,n):
        res, curr = 0, 1
        for _ in range(n):
            prev = res
            res = curr
            curr = prev + curr
        return res

if __name__ == '__main__':
    ans = Solution()
    for i in range(8):
        print(ans.fib(i))
