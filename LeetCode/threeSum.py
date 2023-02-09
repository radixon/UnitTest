def threeSum(nums):
    """
    Given an integer array nums, return all the triplets 
    [nums[i], nums[j], nums[k]] such that i != j, i != k, 
    and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate 
    triplets.
    """
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]: continue
        low, high = i+1, len(nums)-1
        while low < high:
            value = nums[i] + nums[low] + nums[high]
            if value < 0:
                low += 1
            elif value > 0:
                high -= 1
            else:
                res.append([nums[i],nums[low],nums[high]])
                low += 1
                while low < high and nums[low] == nums[low-1]:
                    low += 1
    return res