class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        res = []
        indegree = [0]*n
        for u, v in edges:
            indegree[v] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                res.append(i)
        return res


if __name__ == '__main__':
    res = Solution()
    n = 6
    edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
    print('n: ', n, '\t', 'edges: ', edges)
    print('Output: ',res.findSmallestSetOfVertices(n,edges),'\n')

    n = 5 
    edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
    print('n: ', n, '\t', 'edges: ', edges)
    print('Output: ',res.findSmallestSetOfVertices(n,edges),'\n')