# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 09:34:06 2020
Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3]
Explanation: Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively. It doesn't matter what values are set beyond the returned length.
 

Constraints:

0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in ascending order.

Solution:
    
Use two pointers

i is slow and we increment it one at a time, putting the proper number in its place in
nums. j is a fast pointer, and moves ahead of i to find which number to put at i. We start i
and j at zero, and keep a counter to track how many times we have seen the number at j. 

Every loop through, we increment the count if nums[j] == nums[j-1], otherwise we set the count
to 1. If we find that the count is greater than 2, then j needs to go ahead to find the next
possible element to put at i, so we increment j until nums[j] != nums[j-1]. At this point we
can be satisfied that the count is reset back to 1, and put nums[j] at nums[i]. If we find
that the count was not greater than 2, then nums[j] has not appeared twice yet and can be placed
at i. Then we increment i and j to advance the loop. Finally, we just have some checks in place
to make sure we dont get an index error, and return as soon as j exceeds the length of the array

@author: Robert Xu
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        cur_count = 0
        
        while j < len(nums):
            
            if nums[j] == nums[j-1]: cur_count += 1
            else: cur_count = 1
            
            if cur_count > 2 and nums[j] == nums[j-1]:
                
                while j < len(nums) and nums[j] == nums[j-1]:
                    
                    j += 1
                
                cur_count = 1
                if j > len(nums)-1: return i
            nums[i] = nums[j]
            i += 1
            j += 1
            
            
        return i

ls = [0,0,1,1,1,1,2,2,2,3]
a = Solution()
b = a.removeDuplicates(ls)
        