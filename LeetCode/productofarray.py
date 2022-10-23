def productExceptSelf(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    """
    if nums.count(0) > 1: return [0]*len(nums)
    prefix = suffix = 1
    ans = [1]*len(nums)
    for i in range(len(ans)):
        ans[i] *= prefix
        ans[-i - 1] *= suffix
        prefix *= nums[i]
        suffix *= nums[-i - 1]
    
    return ans