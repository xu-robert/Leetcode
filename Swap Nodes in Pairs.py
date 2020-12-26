# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:16:02 2020
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

Solution
We can solve it either iteratively or recursively, recursive shown. If head is null or head.next is null, we just
return head. THis is the base case. Otherwise, we do the swapping. The only thing we need to be careful of is
making sure we don't create any cycles in our linked list. Other than that, the code is pretty self explanatory.

Temp refers to the node head.next.next, which will be the next node we run the algorithm on after we swap head and 
head.next. Next we swap head and head.next. Since our new head is head.next, we neet to make sure that we refer to 
head.next as head, and keep our old head in another variable. Then we connect head.next to old head, and connect 
old_head.next to the recursive swapPair on temp. 
@author: Robert Xu
"""
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            temp = head.next.next
            old_head = head
            head = head.next
            head.next = old_head
            old_head.next = self.swapPairs(temp)
        
        return head