## Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2. The tests are generated such that there is exactly one solution. You may not use the same element twice.  Your solution must use only constant extra space. <br />

Intuition: In a sorted list the smallest integer is located at index 0 and the largest integer is located at arr.size() - 1.  If you add the two integers one of three outcomes will happen
* The sum is smaller than the target value.  In this case, adding 1 to the smaller index will increase the value of the sum.
* The sum is larger than the target value.  In this case, subtracting 1 from the larger index will decrease the value of the sum.
* The sum equals the target.  In this case, return the pair of indexes + 1.  Add 1 to the return values because the arr is 1-indexed, yet Python is 0-indexed.

 
Time Complexity: O(n) <br />
The worst case is traversing the array once. <br />
Space Complexity: O(1) <br />
Constant space is used to maintain the pointers to the two pointers. <br />

![twosum_II_test](https://github.com/radixon/UnitTest/assets/59415488/54534cc1-4881-464f-9bb8-28e08397b342)
