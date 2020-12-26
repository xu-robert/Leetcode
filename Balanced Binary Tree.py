# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:10:15 2020
Balanced Binary Tree

iven a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Input: root = []
Output: true\
    
Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

Solution:
We want to do this a postorder traversal to get O(n) time complexity. Note that an empty tree is considered balanced.

We just recursively solve postorder(bottom up), and get the height of left and right subtree starting from the leaf nodes.
IIf at any point we encouter a node which is not balanced, we return a height of -1 and false, which will be carried through
until the root. Otherwise, the root will return True.

@author: Robert Xu
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root):
            if root == None: 
                return (0,True)
            
            hleft, bal_left = helper(root.left)
            hright, bal_right = helper(root.right)
            
            if abs(hleft-hright) <= 1 and (bal_left and bal_right):
                return (1 + max(hleft, hright), True)
            
            return (-1, False)
        
        return helper(root)[1]
        