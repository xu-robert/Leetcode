# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:15:52 2020

Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1

Solution:
    
Having done this after learning about the O(nlogn) solution to the longest increasing subsequence
problem, this one is pretty straightforward. That method uses patience sorting with binary search
to find the length of the LIS in O(nlogn) time. Its a pretty tricky concept that doesn't I don't 
really get intuitively, but take it on faith that it works.

So really, the triplet subsequence is the same problem, but with the constraint that we only
need to find whether an LIS of 3 exists, we can improve the time and space complexity 
dramatically to O(n) time and O(1) space.

Using the patience sorting method, We keep an array that just has two entries: To start out,
we both the first and second entry = infinity. 
We iterate through the array, say we are at A[i] = n. 

First we compare n with the second entry of the array. If n is greater, we return True.
Otherwise, we compare with the 1st entry. If n is greater than the 1st entry, we overwrite the
second entry with n. Finally, if n is less than the 1st entry, we overwrite the 1st entry with n.

A better description of patience sorting can be found online, but lets run through the example
nums = [2,1,5,0,4,6]

initial state: arr = [inf,inf]

i = 0, n = 2
Since arr only contains inf, by default after i = 0, arr will always be [nums[0],inf].
Basically by having x non-inf numbers in arr, the longest increasing subsequence so far has 
length of x.

arr = [2,inf] (lis = 1)

i = 1, n = 1
n is less than all entries of arr, so we overwrite arr[0] with 1. What is the implication?
Now if the next element is 2, the algorithm will find that 2 is greater than arr[0], and
place 2 as the 2nd entry of arr, meaning we have an lis of length 2. The first 2 at i = 0 is
no longer relevant for us. 

arr = [1, inf] (lis = 1)

i = 2, n = 5
now we have n > 1st entry of arr, so we overwrite the second entry. By having a non-inf in
the second entry, we are saying that we found an LIS of length 2 (either 2,5 or 1,5 in this case)
If we find any number greater than 5 later, we are sure that we found an LIS of lenth 3

arr = [1,5] (lis = 2)

i = 3, n = 0
n < 1st entry, so overwrite the 1st entry. note that the sequence arr[0], arr[1] does not
necessarily form an LIS. By overwriting the 1st entry with n, we are saying: any number
greater than n can now form an LIS of length 2, that number does not need to be greater than
the old 1st entry that n just replaced. The fact that we still have a non-inf in the second
entry tells us that we still have an LIS of 2, just not one that includes 0 (yet)

arr = [0,5] (lis = 2)

i = 4, n = 4.
n > 1st entry, so we overwrite the second entry. Now the implication is: the length 2 subsequence
no longer needs to end with 5, we found a new length 2 subsequence which ends with 4 (0, 4).

arr = [0,4] (lis = 2)

i = 5, n = 6
Finally we see that n > 2nd entry, so we return True.

@author: Robert Xu
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        
        lis = [float('inf')]*2
        
        for n in nums:
            
            if n > lis[1]:
                return True
            
            elif n > lis[0]:
                lis[1] = n
            
            else:
                lis[0] = n
        
        return False

a = Solution()
b = a.increasingTriplet(nums = [2,1,5,0,4,6])