def maxSubArray(nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    A subarray is a contiguous part of an array.
    """
    ans = -float('inf')
    subarray = 0

    for value in nums:
        subarray = max(subarray+value, value)
        ans = max(subarray, ans)
    return ans