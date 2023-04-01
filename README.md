# UnitTest

This repository will explore creating unit test for Python programs.  Problems solved will come from a variety of sources; including, LeetCode, Project Euler, and others.

# Two Pointer Technique

## Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2. The tests are generated such that there is exactly one solution. You may not use the same element twice.  Your solution must use only constant extra space. <br/ >

Intuition: There is a pointer at the beginning of the array, and a pointer at the end of the array. If the elements of the two indexes sum to be less than the target, increase the sum by increasing the index at the 'low' end. If the elements of the two indexes sum to be greater than the target, reduce the sum by decreasing the index at the 'high' end. If the sum of the two indexes equals the target, output the two indexes + 1 due to the array being 1-indexed.

Time Complexity: O(n) <br />
The worst case is traversing the array once. <br />
Space Complexity: O(1) <br />
There is only constant space added within the algorithm. <br />

## Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).  Find two lines that together with the x-axis form a container, such that the container contains the most water.  Return the maximum amount of water a container can store.<br />

Notice that you may not slant the container.<br />

Intuition: We are looking for the rectangle with the greatest area. As such the limiting factor is the height of the lowest wall per rectangle. This leads to the following steps:
1. Measure the rectangle's area based on the height of the lowest wall.
2. Compare the current area to the max area. If current area > max area, save the current area as the new max area.
3. Move the pointer at the lowest height to continue to give the opportunity for max area on the next iteration.
4. Output the max area found.<br />

Time Complexity: O(n)<br />
Each possible area will have to be checked. This requires traversing the entire array once.<br />

Space Complexity: O(1)<br />
Constant extra space is used to store the two pointers, and the output.<br />

## Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.<br />

## 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. <br />

Notice that the solution set must not contain duplicate triplets. <br />

## Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.<br />

Return true if you can reach the last index, or false otherwise.<br />

Intuition:  The game is looking for a succession of jumps that reaches the end of the array.  There are only two points that matter.  The current index, and the max index of jumps from previous locations.  If the jump from the current index is greater than the max index of previous jumps, update the max index location.  Return true if max index is greater than or equal to the end of the array index before the current index passes the max index; otherwise, return false.<br />

# Binary Search

## Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.<br />

You must write an algorithm with O(log n) runtime complexity.<br />

## Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become: <br />

* [4,5,6,7,0,1,2] if it was rotated 4 times. <br />
* [0,1,2,4,5,6,7] if it was rotated 7 times. <br />
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]]. <br />

Given the sorted rotated array nums of unique elements, return the minimum element of this array. <br />

You must write an algorithm that runs in O(log n) time. <br />

## Find Minimum in Rotated Sorted Array II

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become: <br />

* [4,5,6,7,0,1,4] if it was rotated 4 times. <br />
* [0,1,4,4,5,6,7] if it was rotated 7 times. <br />
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]]. <br />

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array. <br />

You must decrease the overall operation steps as much as possible. <br />

## Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values). <br />

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. <br />

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums. <br />

You must write an algorithm with O(log n) runtime complexity. <br />

## Search in Rotated Sorted Array II

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values). <br />

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4]. <br />

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums. <br />

You must decrease the overall operation steps as much as possible. <br />

# Backtracking

## Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

## Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

## Combination Sum III

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

* Only numbers 1 through 9 are used.
* Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order. <br />
<br />
<br />
<br />
<br />
<br />


## Best Day to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
 <br /><br />   
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. <br />

## Contains Duplicate [Array]

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. <br />

## Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. <br />
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.  You must write an algorithm that runs in O(n) time and without using the division operation. <br />

## Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. <br />
A subarray is a contiguous part of an array. <br />

## Maximum Product Subarray

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product. <br />
The test cases are generated so that the answer will fit in a 32-bit integer. <br />

# Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise. <br />

## TwoSum <br />

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.  You may assume that each input would have exactly one solution, and you may not use the same element twice. <br />
<br />
To solve this problem in O(n) time, sort the array and use the two pointer algorithm or use a hash table to store values.  Note hash tables are called dictionaries in Python.  Hash tables having O(1) lookup for average and amoritized cases.  See section 5.5 Dictionaries of Python documentation, docs.python.org. <br />
