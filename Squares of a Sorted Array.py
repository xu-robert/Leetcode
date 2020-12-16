# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:43:02 2020
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Solution:
Two pointer method, use the absolute value of num[l] and num[r] to add to answer, which
at first will be sorted in decreasing order, so then just reverse it
@author: Robert Xu
"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l,r = 0, len(nums)-1
        ans = []
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ans.append(nums[l]**2)
                l += 1
            
            else:
                ans.append(nums[r]**2)
                r -= 1
        
        return ans[::-1]