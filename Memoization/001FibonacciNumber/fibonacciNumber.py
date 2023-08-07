class Solution():
    memo = {0:0,1:1}
    def fib(self,n: int) -> int:
        if n in self.memo: 
            return self.memo[n]
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]


if __name__ == '__main__':
    ans = Solution()
    for i in range(8):
        print(ans.fib(i))
