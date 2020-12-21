# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 09:56:53 2020
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, 
and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B
 and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000

Solution:

Another challenging daily problem. I think I also peeked at the solution for this one before,
so my solution is informed by that. 

Lets assume that the array is sorted. THe key thing to observe is that for the optimal solution,
there is an index i in the array where all numbers A[0:i] have K added, and all A[i+1:] have -K
added. Either that, or we add K to the entire A, in which case our answer is A[-1] - A[0]. I 
won't offer a proof for why that is here, but it should make sense if you draw a graph of the
sorted elements of A and draw up or down arrows to indicate whether we +K or -K to it.

FOr now we just assume that our array is sorted, and the optimal solution occurs when we flip from
+K to -K at some index i. So we don't know what the optimal value of i is, so we will just
iterate through the whole array and see if our solution at i is better than a previous optimum.

TO solve out problem at i, we assume that everything before and including i (A[:i]) is +K, and
everything after i (A[i+1:]) is -K. Because A is sorted, we can take advantage of this
to find max(A) and min(A) of our transformed A. Since everything after i is -K, we subtract
K from A[-1]. Since its sorted, all A[j]-K between A[i+1] and A[-1] is less than A[-1]-K. So
one potential max for our transformed array is A[-1]-K. The other candidate for max is A[i]+K.
If K is sufficiently large, A[i]+K could be larger than A[-1]-K. And again, since A is sorted,
A[i]+K >= A[j]+K for all j in range(0, i-1). So if we flip from +K to -K after index i, our 
transformed max is max(A[i]+K, A[-1]-K).

Similarly we can find two possible minimums. Either A[i+1]-K (it will be the smallest in the -K
section of the array) or A[0]+K, which is the smallest in the +K section of the array. Now that
we have max and min for flipping after i, we just calculate max-min and see if its greater
than what we currently have in ans. 

Note we only iterate from 0 to i-1. That is, in the for loop we do not consider the case where
we i = len(A) - this is equivalent to adding K to the entire array, leaving us the same answer
as A[-1] - A[0]. Instead, we initialize ans to this value and see if we can beat it at any other
i.

So for the algorithm, all we do is sort the input and use the previously mentioned steps to get 
the opt. 
@author: Robert Xu
"""
class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        
        ans = A[-1] - A[0]
        
        for i in range(len(A)-1):
            
            mn = min(A[0]+K, A[i+1]-K)
            mx = max(A[i]+K,A[-1]-K)
            
            ans = min(ans,mx-mn)
        
        return ans

a = Solution()
b = a.smallestRangeII(A = [0,3,4,7,9,11], K = 5)