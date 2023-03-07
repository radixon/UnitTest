"""
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
def backtrack(path,target,low,high,counter,res):
    if target == 0:
        res.append(path.copy())
        return
    for i in range(low,high):
        if i in counter and counter[i] > 0 and target - i > -1:
            path.append(i)
            counter[i] -= 1
            backtrack(path,target - i,i,high,counter,res)
            counter[i] += 1
            path.pop()

def count(nums):
    track = {}
    for value in nums:
        if value in track:
            track[value] += 1
        else:
            track[value] = 1
    return track

def combinationSum2(candidates, target):
    res = []
    counter = count(candidates)
    backtrack([],target,min(counter),max(counter) + 1,counter,res)
    return res