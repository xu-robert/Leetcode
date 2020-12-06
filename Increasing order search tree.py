# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:27:12 2020
 Increasing Order Search Tree
 
 Just traverse the tree inorder style, everytime we pop a new node, we know its bigger
 than the last one so connect it to the right of the last node.
 
@author: Robert Xu
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        dummy = TreeNode()
        last = dummy
        
        if root == None: return None
        
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                last.right = cur
                last = cur
                cur.left = None
                cur = cur.right
        
        return dummy.right