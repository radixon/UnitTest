def search(nums, target):
    """
    Time Complexity: O(log n)
    The algorithm splits the array in half each iteration.
    
    Space Complexity: O(1)
    Constant extra space is used for variables low, high, and mid.
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
