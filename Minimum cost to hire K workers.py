# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 16:23:41 2020

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000

Quite a confusing question but pretty rewarding to solve. The key observation I had to make is
this: suppose we choose a group of m workers out of the N workers in the pool. Because every
worker is paid according to the relative quality of their work compared to the quality of other
workers in the group. In other words, every worker in the pool is paid according to the same
wage/quality ratio. If worker 2 has 3x quality of worker 1, he gets paid 3x more. In math terms,
for all worker w in group m, the wage of worker m is the quality of worker m * (wage/quality)
ratio of the group.

The question is what is this wage/quality ratio? It turns out that for our pool of m workers,
 every worker gets paid according to the highest w/q ratio among the group members. Lets see why
this is the case. Lets say that worker x in group m has a wage y and quality z. And we will say
that worker x has the highest w/q ratio in the group, that is y/z >= all other w/q ratios in 
group. We can calculate the minimum wage of worker x as w = z*(y/z). So lets say we pick
a different worker in the group to set the group w/q ratio. In this case, x gets paid according
to some (w/q) which is <= (y/z): x gets paid z*(w/q) which is necessarily <= y because 
(w/q) <= (y/z). So for worker x to get paid his minimum wage, the group w/q ratio must be y/z,
which is the highest w/q ratio in the group members. 

Now we have a clearer path to answering our question. We know that for our group of size K, 
the highest w/q ratio among group members will be the group ratio. So our cost for hiring
these k workers is (w/q)*(q1 +q2 + ... qK). Notice that q1..qK must include our group member
who has the highest w/q ratio. So we need to select K-1 other workers who have a w/q ratio LESS
THAN or EQUAL to w/q. Lets denote the wage for this member wx, quality qx. We rewrite
cost = (wx/qx)*(qx + q1 + ... qK-1). How do we minimize the cost? well we want to minimize the
quantity q1 + ....qK-1. Things start to come together at this point. 

We don't know which of the N total workers will result have the optimal w/q ratio for the min
cost, so we will try getting an answer for each x of them, treating them as having the highest
w/q ratio for the group of K. If x has the highest w/q ratio, then we pick the other K-1 group
members with the least sum of quality. In other words, we want the k-1 smallest quality workers
among the N workers with w/q smaller than wx/qx. This part is a heap question! And to guarantee
that we are picking only workers with w/q <= wx, qx, we can sort by the w/q ratio of each worker!

So here is how the algo works. First we zip the w/q arrays into tuples so each worker is
represented by a tuple (w/q). Then we in descending order by the w/q ratio (or ascending by
the q/w ratio, same result). The highest w/q ratio is the 0th element after sorting. Then,
we use a heap to maintain the k-1 smallest qualities mobing backwards through the sorted array.
This ensures that the k-1 smallest qualities come from workers with a lower w/q ratio than the
worker x we choose as the group rep. If the heap size is K-1 at index i, then minimum 
(q1 + ...qK-1) value at index i-1 is the sum of the heap, and we record this in an array

We do one final pass through each worker in the sorted worker array, and evaluate 
(wx/qx)*(qx + q1 + ... qK-1). We record the minimum cost as our ans and voila! 

Special cases: K = 1: we take the worker with the least wage
@author: Robert Xu
"""
import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        if K == 1: return min(wage)
        
        wq_pairs = zip(wage, quality)
        wq_pairs = sorted(wq_pairs, key = lambda x: (x[1]/x[0]))
        
        sum_smallest_arr = [0]*len(wq_pairs)
        
        heap = []
        sum_smallest = 0
        for i in range(len(wq_pairs)-1,0,-1):
            sum_smallest += wq_pairs[i][1]
            heapq.heappush(heap, -wq_pairs[i][1])
            if len(heap) > K-1:
                sum_smallest += heapq.heappop(heap)
            if len(heap) == K-1:
                sum_smallest_arr[i-1] = sum_smallest
        
        ans = float('inf')
        for (w,q), s in zip(wq_pairs, sum_smallest_arr):
            if s == 0:
                return ans
            ans = min(ans, (w/q)*(q+s))
    
a = Solution()
b = a.mincostToHireWorkers([3,1,10,4,10], [4,8,6,3,6], 5)