class Solution():
    """
    Time Complexity: O(n)
    The algorithm traverses the cost array once.
    
    Space Complexity: O(1)
    Constant space is used on the prev, curr, and temp variables
    """
    def minCostClimbingStairs(self, cost) -> int:
        oneStepBehind, twoStepsBehind = 0, 0
        for i in range(len(cost)-1):
            temp = twoStepsBehind
            twoStepsBehind = oneStepBehind
            oneStepBehind = min(temp+cost[i],oneStepBehind+cost[i+1])
        return oneStepBehind

if __name__ == '__main__':
    from random import randint
    ans = Solution()
    cost = [10,15,20]
    print(ans.minCostClimbingStairs(cost) == 15)

    cost = [1,100,1,1,1,100,1,1,100,1]
    print(ans.minCostClimbingStairs(cost) == 6)

    cost = [10,15,20,30,40,60,80]
    print(ans.minCostClimbingStairs(cost) == 105)
