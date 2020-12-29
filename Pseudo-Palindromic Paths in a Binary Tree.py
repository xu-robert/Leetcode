# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:55:57 2020

Given a binary tree where node values are digits from 1 to 9.
 A path in the binary tree is said to be pseudo-palindromic if at least 
 one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root
node to leaf nodes: [2,3,3], [2,1,1], and [2,3,1]. Among these paths [2,3,3] can be rearranged in [3,2,3] 
(palindrome) and the path [2,1,1] can be rearranged in [1,2,1] (palindrome).

Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node
to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only
[2,1,1] can be rearranged in [1,2,1] (palindrome).

Constraints:

The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.

Solution

This question has two parts of understanding: 1: how do we know if a path-permutation can be rearranged into a palindrome
and 2. how do we traverse the tree?

For point 1: There was a similar question which asked: given a string, could the string be rearranged into a palindrome?
This is the same concept. We note that a palindrome has one of two forms: (s1)xx(s2) or (s1)x(s2) where s1 and s2 are
mirror images of one another. Because they are mirror imges, each unique element of s1 appears an even element of times
(n times in s1 and n times in s2). In case 1, the element x appears twice, so a palindrome that follows pattern 1 
consists of unique elements which all appear an even number of times. In contrast, in pattern 2, the element x appears
only once. Note that s1 and s2 may contain the element x as well, so the element x can appear 2n+1 times, where n 
is any integer greater than 0. All elements besides x appear an even number of times. X appears an odd number of times.
In both cases of palindrome, there is at MOST one element which appears an odd number of times - if we are given a
collection of elements, if there is more than one element which appears an odd number of times, there is not a valid 
palindrome which can be made as a permutation of the items in the collection. 

For point 2: We simply traverse the tree in postorder fashion. We have a global resource pathcount, which is an array
of length 10, which we use to store the counts of elements we have seen on the path so far. Each time we visit a node,
we add its value to pathcount and recursively traverse the tree until we hit a leaf node. Once we hit a leaf node, we
use our logic for point 1 to determine whether we can make a palindrome with the elements on this path. If so , we 
increment our answer. Once we finish exploring a node, we backtrack by decrementing the count of its value in pathcount,
which ensures that we do not consider that nodes value on the next path. 


@author: Robert Xu
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pathcounts = [0]*10
        self.ans = 0
        def dfs(root):
            if root:
                self.pathcounts[root.val] += 1
                
                if root.left == None and root.right == None:
                    
                    odds = 0
                    for n in self.pathcounts:
                        if n%2 != 0:
                            odds += 1
                            
                    if odds <= 1:
                        self.ans += 1
                
                dfs(root.left)
                dfs(root.right)
                
                self.pathcounts[root.val] -= 1
        
        dfs(root)
        return self.ans
        