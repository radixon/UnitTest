def twoSum(nums, target):
    """
    Given an array of intergers 'nums' and an integer 'target,' return indicies
    of the two numbers such that the two numbers add up to 'target.'
    """
    detector = {}
    for i in range(len(nums)):
        if nums[i] in detector:
            if detector[nums[i]] < i:
                return [detector[nums[i]], i]
            else:
                return [i, detector[nums[i]]]
        detector[target - nums[i]] = i
    return None