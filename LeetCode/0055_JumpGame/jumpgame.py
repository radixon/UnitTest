def canJump(nums):
    """
    You are given an integer array nums. You are initially positioned 
    at the array's first index, and each element in the array represents 
    your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
    """
    currIndex, maxIndex = 0, nums[0]
    while currIndex <= maxIndex:
        if maxIndex >= len(nums) - 1:
            return True
        if nums[currIndex] + currIndex > maxIndex:
            maxIndex = nums[currIndex] + currIndex
        currIndex += 1
    return False
