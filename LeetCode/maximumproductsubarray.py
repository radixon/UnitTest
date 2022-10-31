def maxProduct(nums):
    """
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, 
    and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.
    A subarray is a contiguous subsequence of the array.
    """
    prefix = suffix = 1
    ans = max(nums)
    for i in range(len(nums)):
        prefix *= nums[i]
        suffix *= nums[-i - 1]
        ans = max(prefix, suffix, ans)
        if prefix == 0: prefix = 1
        if suffix == 0: suffix = 1
    return ans