def search(nums, target):
    """
    Given an array of integers nums which is sorted in ascending order, 
    and an integer target, write a function to search target in nums. If 
    target exists, then return its index. Otherwise, return -1.

    You must write an algorithm with O(log n) runtime complexity
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    nums = [[-1,0,3,5,9,12],
            [-1,0,3,5,9,12]
           ]
    
    target = [9,2]

    for i in range(len(nums)):
        print(search(nums[i],target[i]))
