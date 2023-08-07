class Solution():
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