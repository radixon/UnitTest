def twoSum(nums, target):
    """
    Given an array of intergers 'nums' and an integer 'target,' return indicies
    of the two numbers such that the two numbers add up to 'target.'
    """
    for i in range(len(nums)):
        value = target - nums[i]
        if value in nums:
            j = nums.index(value)
            if i < j:
                return [i,j]
            if j < i:
                return [j,i]
    return None