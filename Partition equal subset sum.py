# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:43:04 2020
Partition equal subset sum

Given a non-empty array nums containing only positive integers, find if the array can be partitioned
into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100


Classic dynamic programming question. Knapsack problem, solve with O(mn) complexity where m is the
partition sum. My approach is bottum up, slower than the top down approach. First, we calculate the 
partition sum, which is just half the sum of the array. If the array sum is not divisible by 2, return
False since we know you cant get two equal halves. 

Create a dp array like the following (for nums [2,2,1,1]):
target = 3

dp
  0 1 2 3
0
2
2
1
1

The dp is initiated with all elements false, except for dp[0][0], which is True. The element dp[i][j]
is true if you can make the number j with some subset of nums[0], ... nums[i]. So dp[0][0] True means
you can make 0 with an empty subset, which is always true (sum of 0 number is 0).

We begin our iteration
at i = 1, so we are seeing which numbers we can make with just nums[0] (i = 1). Our rule is this: if j is
less than nums[i-1], then we know we cant make j by including nums[i-1] in a subset, so dp[i][j] is 
dp[i-1][j]. If j > nums[i-1], we can either include nums[i-1] or not in the current subset, so dp[i][j]
is dp[i-1][j] or dp[i-1][j-num]. dp[i-1][j] is True if we can make j with nums[:i-1] (we dont include nums[i]
in the current subset). dp[i-1][j-num] is true if we can make j-num with nums[i-1] (we include nums[i] in
                                                                                    the current subset)
Finally we return True if dp[-1][-1] is true. 

@author: Robert Xu
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = sum(nums)
        
        if x % 2 != 0: return False
        
        dp = [[False for _ in range(x//2+1)] for _ in range(len(nums)+1)]
        
        dp[0][0] = True
        
        for i in range(1, len(nums)+1):
            num = nums[i-1]
            for j in range(x//2 + 1):
                if j < num:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-num] or dp[i-1][j]
        
        return dp[-1][-1]
a = Solution()
b = a.canPartition([2,2,1,1])