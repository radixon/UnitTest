def findMin(nums):
    """
    Suppose an array of length n sorted in ascending order 
    is rotated between 1 and n times. 

    Given the sorted rotated array nums that may contain 
    duplicates, return the minimum element of this array.

    You must decrease the overall operation steps as much 
    as possible.
    """
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        
        if nums[mid] == nums[high]:
            nums.pop()
            high -= 1
        elif nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]