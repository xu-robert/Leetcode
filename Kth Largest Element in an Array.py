# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 08:42:43 2021

Classic heap problem: lots of better explanations online. 
The key is that even though we want the kth LARGEST number, we maintain a heap with the SMALLEST number at the top
of the heap ( a min heap). When the heap reaches size k (or length k), this means that the top element is the kth
largest (smaller than all the other elements in the heap). If we exceed length k, we need to pop the smallest element
from the heap - though we always maintain that the top element is the smallest in the heap, and the k - largest elements
processed so far are in the heap.

@author: Robert Xu
"""
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []
        
        for n in nums:
            
            heapq.heappush(heap, n)
            
            if len(heap) > k:
                
                heapq.heappop(heap)
        
        return heapq.heappop(heap)

a = Solution()
b = a.findKthLargest([3,2,1,5,6,4], 2)