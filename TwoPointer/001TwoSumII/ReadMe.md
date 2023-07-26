## Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2. The tests are generated such that there is exactly one solution. You may not use the same element twice.  Your solution must use only constant extra space. <br />

Intuition: There is a pointer at the beginning of the array, and a pointer at the end of the array. If the elements of the two indexes sum to be less than the target, increase the sum by increasing the index at the 'low' end. If the elements of the two indexes sum to be greater than the target, reduce the sum by decreasing the index at the 'high' end. If the sum of the two indexes equals the target, output the two indexes + 1 due to the array being 1-indexed.

Time Complexity: O(n) <br />
The worst case is traversing the array once. <br />
Space Complexity: O(1) <br />
There is only constant space added within the algorithm. <br />
