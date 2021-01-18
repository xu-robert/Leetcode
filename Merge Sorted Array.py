# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:43:43 2021
Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
 

Constraints:

0 <= n, m <= 200
1 <= n + m <= 200
nums1.length == m + n
nums2.length == n
-109 <= nums1[i], nums2[i] <= 109

Solution
THis is the type of question I hate on leetcode. No problem solving really, just take a really easy concept and
turn in into a dumb situation. I didn't bother writing an O(n) solution cause this question is dumb, just copy nums2 
into nums1 and sort. Anyway the constraints are small enough so it wont time out.
@author: Robert Xu
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()

nums1 = [0]
a = Solution()
b = a.merge(nums1, m = 0, nums2 = [1], n = 1)