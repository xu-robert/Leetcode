# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:55:25 2020
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

Solution:
Basically an extension of the 2sum approach, which we can solve in O(n) time. 4sum we can solve
in O(n^2) time. 

We use a hashtable (defaultdict) to keep counts of the different combinations of A and B elements
For each element a in A, we iterate through elements b of B. for each a,b combination, we increment
the dictionary entry for a+b. By the end of this step, we will know how many ways we can make
each a+b combination. There may be 4 ways to make -1 by adding different elements of A and B for
example. We will call this hashtable ab.

Next, we similarly iterate through elements c in C and d in D. For each c+d combination, we 
increment ans by ab[-(c+d)], because if c+d is 4, then we look for the number of ways we can
make -4 using A and B, and 4 + (-4) = 0. Lets say we have c+d = 4, and ab[-4] = 5. This means
that there are 5 A[i], B[j] combinations in A and B that sum to 4. Which means that for this
particular C[k] + D[l] combination, there are 5 ways to reach 0 with elements from A and B.
 If we come
across a different c+d combination that also equals to 4, then we add another 5 to ans because
that c+d combination corresponds to different k and l.

@author: Robert Xu
"""
from collections import defaultdict

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ab = defaultdict(int)
        
        for a in A:
            for b in B:
                ab[a + b] += 1
        
        ans = 0
        for c in C:
            for d in D:
                ans += ab[-(c+d)]
        
        return ans
a = Solution()
A = [-1,-1,0,1,2,3]*100
B = [-4,-3,1,2,3,3]*100
C = [-6,0,1,1,2,5]*100
D = [-6,3,4,4,4,6]*100
b = a.fourSumCount(A, B, C, D)