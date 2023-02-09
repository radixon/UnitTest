"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a 
container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
def maxArea(height):
    low, high = 0, len(height) - 1
    res = 0
    while low < high:
        if height[low] < height[high]:
            res = max(height[low]*(high-low),res)
            low += 1
        else:
            res = max(height[high]*(high-low),res)
            high -= 1
    return res
