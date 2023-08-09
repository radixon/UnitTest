class Solution:
    """
    Time Complexity: O(n)
    The algorithm traverses the cost array once.
    
    Space Complexity: O(n)
    The memo hashmap will grow linearly with the cost array.
    """
    def minCostClimbingStairs(self, cost):
        self.memo = {0:0,1:0}
        self.cost = cost
        return self.climbingStairs(len(cost))
    
    def climbingStairs(self,n):
        if n in self.memo:
            return self.memo[n]
        oneStepJump = self.cost[n-2] + self.climbingStairs(n-2)
        twoStepJump = self.cost[n-1] + self.climbingStairs(n-1)
        self.memo[n] = min(oneStepJump,twoStepJump)
        return self.memo[n]

if __name__ == '__main__':
    from random import randint
    ans = Solution()
    cost = [10,15,20]
    print(ans.minCostClimbingStairs(cost) == 15)

    cost = [1,100,1,1,1,100,1,1,100,1]
    print(ans.minCostClimbingStairs(cost) == 6)

    cost = [10,15,20,30,40,60,80]
    print(ans.minCostClimbingStairs(cost) == 105)