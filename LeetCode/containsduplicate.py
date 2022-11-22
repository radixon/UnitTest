def containsDuplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    """

    detector = set()
    for value in nums:
        if value in detector:
            return True
        detector.add(value)
    return False