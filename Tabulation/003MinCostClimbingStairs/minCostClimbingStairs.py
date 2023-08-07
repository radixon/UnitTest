class Solution():
    def minCostClimbingStairs(self, cost) -> int:
        prev, curr = 0, 0
        for i in range(len(cost)-1):
            temp = prev
            prev = curr
            curr = min(temp+cost[i],curr+cost[i+1])
        return curr

if __name__ == '__main__':
    from random import randint
    ans = Solution()
    cost = []
    for i in range(5):
        cost.append(randint(0,25))
    print(cost)
    print(ans.minCostClimbingStairs(cost))

    cost = []
    for i in range(10):
        cost.append(randint(0,50))
    print(cost)
    print(ans.minCostClimbingStairs(cost))

    cost = []
    for i in range(15):
        cost.append(randint(0,100))
    print(cost)
    print(ans.minCostClimbingStairs(cost))