# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:49:47 2020
 Constrained Subsequence Sum
 
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Solution:
This is another monotonic queue question. It boils down to: we dont know exactly which numbers
will be in the subsequence, but we evaluate the max subsequence sum we can reach by first 
evaluating f([0:1]), then f([0:2]), ...f([0:end])

Lets take an example:
nums = [-10,3,2,-9,4,-8,-10,27], k = 3

We try to find the max, following the constraints, by incrementing i, and at each
turn considering nums[i] to be the last element of the subsequence. 
Also note the dynamic programming aspect
when we consider the possible subsequence sums for index i, we look back at the last k elements
to select the previous element in our subsequence. With nums[i] partof the max subsequence,
the max subsequence will be max(nums[i] + maxseq(j) for j in [i-k:i]).

i = 0:
nums[i] = -10
maxseq(i) = -10

i = 1
nums[i] = 3
possible subsequence sums:
-10+3, 3
maxseq(i) = 3

i=2
nums[i] = 2
possible subsequence sums
-10+3+2, 2+3, 2
maxseq(i) = 5

i = 3
nums[i] = -9
possible subsequence sums
-10+3+2-9, 2+3-9,2-9,-9
maxseq(i) = -4

i = 4
nums[i] = 4
possible subsequence sums: Now, -10 is no longer in reach
4+3, 4+5, 4-4,4
maxseq(i) = 9

... and so on...

The structure of the solution lends itself very nicely to a monotonic queue solution to keep
track of the relevant max subsequences for the i-k:i elements. Essentially we use a deque
that stores [(maxseq(j), j)]. We keep the queue monotonic decreasing: lets say
maxseq(m) > maxseq(n) where m > n. Then we no longer need to consider maxseq(n), because any
sequence which can reach n can also reach m, and since maxseq(m) is greater, maxseq(n) will
never give us a better solution. Due to the monotonic nature, then largest subsequence in i-k:i
is at the front of the queue, so we know the optimal solution including nums[i] is 
nums[i] + q[0][0]. If if reach i such that i-q[0][1] > k, then the front element of the queue
cant be selected since it violates the constraint, so we popleft and continue with the queue,
which would now be empty or have the second largest element at the front. A final note is:
if nums[i] is greater than the front element of the queue, the optimal sequence ending at i
meeting the k constraint is just nums[i].

Another note: with k = 1, we are just solving for the max subarray sum. 


@author: Robert Xu
"""



from collections import deque

class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = deque([])
        
        ans = float('-inf')
        
        for i, num in enumerate(nums):
            
            if q and i - q[0][1] > k:
                q.popleft()
            
            if not q:
                q.append((num, i))
                
            else:
                x = max(num, num + q[0][0])
                while q and x > q[-1][0]:
                    q.pop()
            
                q.append((x, i))
                
            ans = max(ans, q[0][0])
        
        return ans

a = Solution()
b = a.constrainedSubsetSum(nums = [10,-2,-10,-5,20], k = 2)