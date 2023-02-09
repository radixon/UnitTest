def findMin(nums):
    """
    Suppose an array of length n sorted in ascending order 
    is rotated between 1 and n times. 

    Given the sorted rotated array nums of unique elements, 
    return the minimum element of this array.  You must write 
    an algorithm that runs in O(log n) time.
    """

    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            low = mid + 1
        else: 
            high = mid
    
    return nums[high]
