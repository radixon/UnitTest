"""
Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it can trap 
after raining.
"""
def trap(height):
    low, high = 0, len(height) - 1
    res, leftMax, rightMax = 0, 0, 0
    while low < high:
        if height[low] < height[high]:
            if height[low] > leftMax:
                leftMax = height[low]
            else:
                res += leftMax - height[low]
            low += 1
        else:
            if height[high] > rightMax:
                rightMax = height[high]
            else:
                res += rightMax - height[high]
            high -= 1
    return res
