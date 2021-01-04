# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:56:59 2021
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together 
the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

SOlution

Classic question. We initialize a dummy node and a cur variable to point to this node,
 then traverse the two linked lists we need to merge. Call these lists
l1 and l2. We only merge while BOTH lists still contain nodes, ie we havent reached the end of BOTH lists. The merging
procedur simply compares the values of node l1 and node l2. If l1 is less than or equal, we point cur.next to l1
and advance our l1 to l1.next. Otherwise, we do the same but for l2. Once a node is added to cur.next, we set cur to
cur.next. We terminate
the merging procedure if we exhaust a list. This is because we can be sure at this point that all the nodes in the
remaining list are greater than or equal to the nodes we have collected in our merged list so far. 

The last step is to set cur.next to l1 or l2. DUe to our while loop condition, we either have l1 = None, l2 != none;
l1 != none, l2 = none; or l1 = None and l2 = None. In whichever case, we have at most one of l1 or l2 != None. So we
set cur.next = l1 or l2, which either merges the erst of l1, l2, or none to cur.next.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode()
        cur = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
                
            cur = cur.next
        
        cur.next = l1 or l2
        
        return dummy.next
        
        
                
        