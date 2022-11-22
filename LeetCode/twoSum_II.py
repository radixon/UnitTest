def twoSum(nums,target):
    """
    Given a 1-indexed array of integers numbers that is already 
    sorted in non-decreasing order, find two numbers such that 
    they add up to a specific target number. The tests are 
    generated such that there is exactly one solution. You may 
    not use the same element twice.

    Your solution must use only constant extra space.
    """

    low = 0
    high = len(nums) - 1
    while low < high:
        value = nums[low] + nums[high]

        if value > target:
            high -= 1
        elif value < target:
            low += 1
        else:
            return [low + 1, high + 1]
    return [None, None]