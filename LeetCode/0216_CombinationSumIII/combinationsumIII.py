"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

    Only numbers 1 through 9 are used.
    Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order.
"""
def backtrack(path,idx,target,k,res):
    if target == 0 and len(path) == k:
        res.append(path.copy())
        return
    for i in range(idx,10):
        if target - i > -1 and len(path) < k:
            path.append(i)
            backtrack(path,i+1,target-i,k,res)
            path.pop()

def combinationSum3(k, n):
    res = []
    backtrack([],1,n,k,res)
    return res
