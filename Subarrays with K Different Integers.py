# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:26:07 2020

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
@author: Robert Xu

Solution I: 

This is a sliding window problem. Ill talk about my solution first, then one that has better space 
complexity than mine.

My solution uses 3 pointers and 2 count arrays. Lets look at an example: arr = [5,0,1,2,1,2,0,1,3], k = 3

At each iteration of the sliding window, we expand the right bound of the window by 1. The goal is to
count how many subarrays with K distinct elements end at this right bound. For example, the window at
j = 6 ,[5,0,1,2,1,2,0], has 4 of these which end at the last 0: 
    [0,1,2,1,2,0],[1,2,1,2,0],[2,1,2,0], and [1,2,0].

There are two important things to note: all of the sliding windows have lower bounds greater than i >= 1.
At i = 0, any subarray ending at j = 6 contains 4 distinct elements (1,2,0,5). All of the windows have
lower bound k <= 4. At k > 4, the window has less than K distinct elements. So for a window ending at j,
if we know i and k, we know how many K-distinct number subarrays end at j. i is the earliest index at 
which K distinct numbers can be found in nums[i:j]. j is the latest index at which K distinct numbers
can be found in [k:j]. So the task is how we find i and k. 

We can do this with two sliding windows with the same upper bound but two different lower bounds.
The rule for shrinking the first window (i): if the number of distinct numbers in the i window exceeds K,
we shrink the window until only K unique numbers are in the window i:j. Each time we shrink the window,
we decrement the i_count of the ith element by one. If the new count is zero, we can decrement the count
of unique numbers in the i:j window. 

THe rule for shirnking the second window (k): k points to the last possible index at which there are K
unique numbers in window k:j. In the k_count[arr], the element that k points to will always have a count
of 1. If the new element at j causes there to be > K unique number is k:j, that means we can increment
decrease the k_count of the kth element by 1 to 0, meaning there are K unique numbers in k:j now. 
However, we want the last k at which k:j still has K unique numbers, so we shrink the k window
and decrement the k_count until the element k points at has a count of 1. This means if we shrink the k
window any smaller, we would have K-1 unique elements in window k:j. 

Once we have finished processing the window, we check if we do indeed have K unique elements in the
in both i:j and k:j. If we do, we can increment our ans by k-i+1. If not, our window does not contain
enough elements yet. 

Solution II: 
Cleaner but it requires that you make the observation that the num of subarrays with exactly K distinct
elements is equal to 
the num of subarrays with at MOST K distinct elements - num of subarrays with at MOST K-1 distinct 
elements. So you just need to solve a simpler sliding window problem twice.

NOTE: in both cases we can just a len(A)+1 length array to store our counts due to the constraints.
"""
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i_count = [0]*(1+len(A))
        k_count = [0]*(1+len(A))
        n_unique = 0
        ans = 0
        i = 0
        k = 0
        
        for j in range(len(A)):
            
            n = A[j]
            i_count[n] += 1
            k_count[n] += 1
            if i_count[n] == 1:
                n_unique += 1
            
            if n_unique > K:
                k_count[A[k]] -= 1
                k += 1
                
            while k_count[A[k]] > 1:
                k_count[A[k]] -= 1
                k += 1

            while n_unique > K:
                i_count[A[i]] -= 1
                if i_count[A[i]] == 0: 
                    n_unique -= 1
                i += 1
            
            if n_unique == K:
                ans += k-i+1
        
        return ans
    
    def subarraysWithKDistinctII(self, A, K):
        
        def atMostK(A, K):
            i = 0
            counts = [0]*(1+len(A))
            n_unique = 0
            ans = 0
            
            for j in range(len(A)):
                counts[A[j]] += 1
                if counts[A[j]] == 1:
                    n_unique += 1
                
                while n_unique > K:
                    counts[A[i]] -= 1
                    if counts[A[i]] == 0:
                        n_unique -= 1
                    i += 1
                ans += j-i+1
            return ans
        
        return atMostK(A, K) - atMostK(A,K-1)
    
a = Solution()
b = a.subarraysWithKDistinct([1,2,1,2,0,3,2,3,1], 4)
            
        
        