# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:29:53 2020
632. Smallest Range Covering Elements from K Lists

You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
Example 3:

Input: nums = [[10,10],[11,11]]
Output: [10,11]
Example 4:

Input: nums = [[10],[11]]
Output: [10,11]
Example 5:

Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

Full disclosure, I could not have solved this without checking discussion and seeing people use a heap ..

Anyway its a very interesting problem which I hope to revisit and hopefully make a video out of

THe idea is that we maintain a heap of k elements, where k is the number of lists we have. The other idea
is that any range covering at least one element from the k lists must have a lower (and upper bound).
The lower and upper bound must both be elements found in nums. So we have two data structures: a k-size
heap, and an array that stores the current pointer for each list in nums. Initially, all pointers are at
zero, and the heap contains the smallest (left most element) in each k list. The initial range is the
smallest item in the heap (head of heap) and the max num in heap. This initial range also has the 
Smallest lower bound of all possible ranges. THis is important.

In each step through the loop, we build the smallest possible range with next smallest lower bound. So
we pop an element from the heap, check which row in nums it belonged to, advance the pointer for that row.
and add the element pointed to into the heap and update the upper bound of the range accordingly. The
range indicated by the current configuration of the heap is now the new heap head, and whatever the max
is. If our current range is less than whatever ans is, we update ans. Now, an important concept is that
the moment any of our pointers exceeds the length of the row its responsible for, we terminate. Why?

Remember that we are finding ranges from in ascending order of their lower bounds. If we exceed the length
of one of our rows, that means our next lower bound is GREATER than the LARGEST element in that row. In
other words, a range with that lower bound can not include an element from the row that our pointer 
exceeds the length of, which violates the goal of the problem. So when this occurs, we terminate because
we have exhausted our search space of possible lower bounds. 

"""

import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        idx = [0]*len(nums)
        
        heap = []
        mx = float('-inf')
        ans = [float('-inf'), float('inf')]
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i))
            mx = max(mx, nums[i][0])
        
        while True:
            lower, row = heapq.heappop(heap)
            if mx - lower < ans[1] - ans[0]:
                ans = [lower, mx]
            idx[row] += 1
            if idx[row] >= len(nums[row]): break
            heapq.heappush(heap, (nums[row][idx[row]], row))
            mx = max(mx, nums[row][idx[row]])
        
        return ans
