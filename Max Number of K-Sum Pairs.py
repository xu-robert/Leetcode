# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:36:19 2021

Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109

Solution

This is just two sum with the twist that we want to count all pairs. All we do is iterate through nums and keep
a dictionary of items we have seen before and their counts. If we are at element with value n, we check to see if
k-n has a count > 0 in our counts dictionary. If it is, then because n + k - n = k (our target), then we know
there is a previously unused element to pair up with the current element. So we increment ans and DECREMENT counts[k-n].
THis is so we know we've used up one element with value k-n, which can't be used again. 

If k-n has count <= 0, then the element n cant be paired up with a number we have seen so far. So we increment its value
in count and continue iterating. Its possible now that it will be paired up with a later number.


@author: Robert Xu
"""

from collections import defaultdict

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        counts = defaultdict(int)
        
        ans = 0
        
        for n in nums:
            
            if counts[k-n] > 0:
                
                counts[k-n] -= 1
                ans += 1
            
            else:
                counts[n] += 1
        
        return ans

a = Solution()
b = a.maxOperations(nums = [3,1,3,4,3], k = 6)