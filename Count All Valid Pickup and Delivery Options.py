# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:34:13 2020

Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90
 

Constraints:

1 <= n <= 500

Solution
I did not do this problem on my own, taken from a post in the discussion. It comes down to a combinatorics problem
with a bit of dynamic programming.

Our base case is n = 1, in which case the only solution is P1D1.

For n = 2, We note that there are three spaces where we can put P2:

_ P1 _ D1 _

P2 P1 D1
P1 P2 D1
P1 D1 P2

And once we place P2, there are four spaces where we can put D2 for each placement of P2:

_ P2 _ P1 _ D1 _
_ P1 _ P2 _ D1 _
_ P1 _ D1 _ P2 _

So in total, there are (number of valid combinations for n = 1)*3*4 = 12 permutations. HOWEVER, in half of these
permutations, we would find that D2 comes BEFORE P2, making it an invalid option. You could write out the 
permutations so this is clear. So we actually have 12/2 = 6 options for n = 2.

Following the same pattern for n = 3.. For each of the 6 valid permutations for n = 2, there are 5 positions to place P3
and 6 positions to place D3 after we place P3. Half of these are invalid, giving us f(3) = 6*5*6/2 = 90.

Generally, f(n) = f(n-1)(2n-1)(2n)/2
    
@author: Robert Xu
"""
class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """

        last = 1
        
        for i in range(2, n+1):
            last = last*(2*i-1)*(2*i)/2
        
        return last % (10**9+7)