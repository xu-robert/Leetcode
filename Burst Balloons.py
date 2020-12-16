# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:57:51 2020

Burst Balloons

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it
 represented by array nums. You are asked to burst all the balloons. If the you burst
 balloon i you will get nums[left] * nums[i] * nums[right] coins.
 Here left and right are adjacent indices of i. After the burst, the left and right 
 then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
             

Solution
This was quite a challenging problem, even though I peeked at someones solution..the key idea is
that we dont ask: whats the most coins I can get if I pop this balloon first? instead it is
whats the most coins I can get if I pop this balloon last?

When we ask the first question, we have a subset problem since for example:

L0: f([3,1,5,8])
L1: Need to solve f([1,5,8]), f([3,5,8]), f([3,1,8]), f([1,5,8])
L2: Need to solve f([1,5]), f([1,8]), f([5,8]), f([3,8]), f([3,5]), f([3,1])
L3: Need to solve f([1]), f([5]), f([8]), f([3])

Where eg f([1,5,8]) = max(1*1*5 + f([5,8]), 1*5*8 + f([1,8]), 5*8*1 + f([1,5]))

Which is 2^4 computations, even with memoization. 

But as it turns out, if we ask the second question, we just need to solve the following 
subproblems:

L0:  f([1]), f([5]), f([8]), f([3])
L1: f([3,1]), f([1,5]), f([5,8])
L2: f([3,1,5]), f([1,5,8])
L3: f([3,1,5,8])

Which is on the order of O(n^2) subproblems, although the solution itself is O(n^3)
The explanation is more difficult than for the O(2^n) solution, but it makes sense, though to me
its not clear why exactly we can use the reverse logic to improve the solution.

Also notice that the levels fit on a grid like so, which forms our dp array:

[0,1,2,3]
[x,0,1,2]
[x,x,0,1]
[x,x,x,0]

where dp[i][j] is the solution to our subproblem corresponding to arr[i:j]. The way we solve
the problems is this: when we solve a subproblem for [i:j], we imagine that no balloons outside
[i:j] have been popped yet: crucially, this means that the boundary balloons arr[i-1] and 
arr[j+1] are intact. Accordingly then, the question to ask is: what is the max score I can
get from arr[i:j], assuming these boundary balloons are intact?

To answer that, we ask: which balloon k in range (i, j) if popped last, will give the max score
for arr[i:j]?

And to finally answer all these questions, we consider this: if balloon k in range (i,j) is the
last balloon to be popped in i:j, the score we get from popping k is arr[i-1]*arr[k]*arr[j+1],
since the boundaries are intact. But then this creates two subproblems: f([i:k-1]) and 
f([k+1:j]). But, we already have solutions to these subproblems if we built our dp correctly!
Because we assume that subproblem i:j has its boundary balloons intact, when we look for
f([i:k-1]) and f([k+1:j]), the solution to these problems assumes that arr[k] is intact. And 
because when we solved f([i:j]) at balloon k, we said that balloon k would be the LAST balloon
in i:j to be popped, our condition that balloon k is unpopped when we solve our two subproblems
is still met. 

Maybe it will make more sense to use an example: (1) [1,2,3,4,9,8,7,6,5] (1).

Lets say we are solving the whole problem f([0:8]), and our k is 4: that is, we are
trying to find the max coins we get if we pop balloon with value 9 last. In that case,
we know that when we go to pop balloon 9, the only balloons left are the phantom ones on the 
edges with value 1. So we know that we can 1*9*1 from that last pop. But if 9 was the last
to be popped, then all the balloons to the left and right of 9 needed to be popped first.
The max coins we could have got by popping 9 last is 1*9*1 plus f([0:3]) and f([5:8]),
which we can draw as (1) [1,2,3,4] (9) and (9) [8,7,6,5] (1), which will have been solved already

Lets walk through the xample [3,1,5,8]

First we solve the L0 subproblems: This case is trivial since the subproblem only consists of
one balloon. If the balloon with index i is the last to be popped in the range i:i, with its
boundaries intact, then since its boundaries are intact, dp[i][i] is just arr[i-1]*arr[i]*arr[i+1]
(with consideration for the boundaries).

[3,1,2,3]
[x,15,1,2]
[x,x,40,1]
[x,x,x,40]

Then we solve the L1 subproblems: consider (1) [3,1] (5) or f([0:1]). We can either pop balloon
with value 3 last, or balloon with value 1 last. If we pop 3 last, we collect 1*3*5 coins from
popping it. There are no balloons to the left of 3, so we collect no coins from the left side
but since there is the balloon with val 1 on its right, we can collect dp[1][1] coins from it.
This is represented by (3) [1] (5) = 15. So by popping the 3 last, we can achieve 1*3*5 + 15
= 30. Similarly, by popping 1 last, we can get 1*1*5 = 5 from popping 1, and solve (1) [3] (1) or
dp[0][0] to add 3 coins, so 8 in total. The max is 30, so dp[0][1] = 30. We fill in the
rest of the L1 problems the same way

[3 ,30,2  , 3]
[x ,15,135,2]
[x ,x ,40 ,48]
[x ,x ,x  , 40]

The L2 problems are much the same: Take (1) [3,1,5] (8) for example. If we pop 3 last, we get
1*3*8 + (3) [1,5] (8) coins, the latter is just dp[1][2]. If we pop 1 last, we get
1*1*8 + (1) [3] (1) + (1) [5] (8), which is dp[0][0] and dp [2][2] respectively. We get 
dp[0][2] = 159

[3 ,30,159, 3]
[x ,15,135,159]
[x ,x ,40 ,48]
[x ,x ,x  , 40]

Finally, L3 is our original problem (1) [3,1,5,8] (1). We try either popping 3 last, or 1, or 5
or 8, and our max is 167, which we return.

[3 ,30,159, 167]
[x ,15,135,159]
[x ,x ,40 ,48]
[x ,x ,x  , 40]

For the algorithm itself, its pretty straightforward: we iterate through the diagonals,
using the observation that each diagonal L0, L1, L2, L3 is associated with a value n, which is
n = j-i (for all L0, j-i = 0, for all L1, j-i = 1). If i == j (or n == 0), this is our base case.
Otherwise, we consider if the balloon k has any left or right balloons in i:j. if k == i,
then there are no balloons to the left, and we just need to lookup the subproblem for the
right balloons. Similarly, we check if k == j, in which case we just lookup the left subproblem.
Otherwise, we have left and right subproblems, and need to lookup both. We can clean those
if/elif blocks, but I havent here. 
@author: Robert Xu
"""
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        for n in range(len(nums)):
            for i in range(len(nums)-n):
                j = i+n
                left = nums[i-1] if i > 0 else 1
                right = nums[j+1] if j < len(nums)-1 else 1
                
                if i == j:
                    dp[i][j] = left*nums[i]*right
                
                else:
                    for k in range(i, j+1):
                        if k == i:
                            dp[i][j] = max(dp[i][j], left*nums[k]*right + dp[i+1][j])
                        elif k == j:
                            dp[i][j] = max(dp[i][j], left*nums[k]*right + dp[i][j-1])
                        else:
                            dp[i][j] = max(dp[i][j], dp[i][k-1] + left*nums[k]*right + dp[k+1][j])
        
        return dp[0][-1]

a = Solution()
b = a.maxCoins([3,1,5,8])