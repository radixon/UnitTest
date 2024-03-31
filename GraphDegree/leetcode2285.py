from collections import defaultdict

class Solution:
    def maximumImportance(self, n, roads):
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        res = 0
        for i in range(n):
            res += degree[i] * (i+1)
        return res


if __name__ == '__main__':
    ans = Solution()
    n = 5
    roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    print("Output: ", ans.maximumImportance(n,roads),'\n')

    n = 5
    roads = [[0,3],[2,4],[1,3]]
    print("Output: ",ans.maximumImportance(n,roads))