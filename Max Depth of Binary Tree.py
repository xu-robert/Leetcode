# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 08:38:19 2020
Max depth of binary tree

If no root, return 0, otherwise depth is at least 1, plus the max depth on the left or right side.
@author: Robert Xu
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))