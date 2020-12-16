# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 08:50:59 2020
Validate Binary Search Tree

Typical inorder traversal question, we know that for a binary search tree an inorder traversal
should yield the results in increasing order. So we keep a variable that has the value of the
last node we visited, and when we visit the next node, we just need to make sure that its greater
than our last value, then set the last value to the value of our current node. 
@author: Robert Xu
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        last = float('-inf')
        
        cur = root
        stack = []
        
        while cur or stack:
            
            if cur == None:
                
                cur = stack.pop()
                if cur.val <= last:
                    return False
                
                last = cur.val
                cur = cur.right
            
            else:
                stack.append(cur)
                cur = cur.left
        
        return True