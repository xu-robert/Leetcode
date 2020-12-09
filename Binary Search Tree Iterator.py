# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:24:32 2020
Binary Search Tree Iterator

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.
 

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

Solution:
    
We just make use of our iterative inorder traversal to traverse the tree. Initialize the tree
with a node nxt, a node cur, and an empty stack.

When next is called, we initiate our inorder traversal, adding the cur node to the stack
and moving left through the tree, adding nodes to stack until we reach None. At this point,
we pop a node off the stack: this will be the node whose value we return from the next function.

We then set the node cur to point and nxt.right. WHen we call next again, the inorder traversal
starts from this node. If we ever reach a point where cur is None and there are no elements
in the stack, this means we have reached the rightmost node in the tree, and hasNext will return
False. 

@author: Robert Xu
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.cur = root
        self.next = None


    def nxt(self):
        """
        :rtype: int
        """
        if self.cur == None and len(self.stack) == 0:
            self.next = None
            return None
        
        while self.cur or self.stack:
            if self.cur == None:
                self.next = self.stack.pop()
                self.cur = self.next.right
                break
            else:
                self.stack.append(self.cur)
                self.cur = self.cur.left
        
        return self.next.val
            

    def hasNext(self):
        """
        :rtype: bool
        """
        if (len(self.stack)>0) or (self.cur):
            return True
        return False
        
a = TreeNode(7)
b = TreeNode(3)
c = TreeNode(15)
d = TreeNode(9)
e = TreeNode(20)

a.left = b
a.right = c
c.left = d
c.right = e

x = BSTIterator(a)
print(x.nxt())
print(x.nxt())
print(x.nxt())
print(x.nxt())
print(x.nxt())
print(x.hasNext())


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()