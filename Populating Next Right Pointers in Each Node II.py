# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:17:49 2020
Populating Next Right Pointers in Each Node II

To do this with constant space and O(n) time, we go level by level, moving left through each the current level. 
At each level, we connect the next nodes in the level beneath.
TO do so, we need to keep track of the leftmost node in the next level, and have a last pointer which
keeps track of the last node we joined in that level. WHen we run out of next nodes in the current level, we switch
to the next level and repeat the process.
@author: Robert Xu
"""

# Definition for a Node.

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        leftmost = None
        last = None
        cur = root
        
        while cur:
            
            if cur.left:
                if leftmost == None:
                    leftmost = cur.left
                else:
                    last.next = cur.left
                last = cur.left
            
            if cur.right:
                if leftmost == None:
                    leftmost = cur.right
                else:
                    last.next = cur.right
                last = cur.right
            
            if cur.next == None:
                cur = leftmost
                leftmost = None
                last = None
            
            else:
                cur = cur.next
        return root
                    