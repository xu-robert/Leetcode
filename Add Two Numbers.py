# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 09:35:35 2021

Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Solution

I have two helper functions here: one converts a non empty list to a the head of its representative linked list
THe other prints the values of a linked list

Actually, all we need to do is traverse each linked list simultaneously, add their values, and note whether or not
we carry a number (if l1.val + l2.val > 10). Dont worry about the fact that its reversed.

There are two things we should consider additionally. THe first is if we reach the end of both lists, but carry = 1.
In this case we just add a node with value 1 to the end. The second is if the lists are not the same length. In this
case we just add 0.

Algo:
Create a dummy node. The next field of the dummy node will point to the linked list we return. Initialize carry = 0,
since when we add the first two numbers there is naturally no carry. Begin traversing l1 and l2. The value of our
new node in our return linked list is equal to the one's digit of
 l1.val (if l1 else 0) + l2.val(if l2 else 0) + carry (just like normal addition rules). The carry for the next two
 nodes is equal to 1 if the above value is greater than or equal to 10, and 0 otherwise. To get both the new value
 and carry in a single operation, we use: carry, val = divmod(a+b+carry, 10) where a = l1.val if l1 else 0 and same for
 b. After we calculate val, we create our new node and advance our pointer for the return linked list, l1, and l2,
 and continue
looping until both l1 and l2 are empty. Finally, we check if we carried a one to the last node. If we did, we add
a new node with value 1. Finally we just return dummy.next

@author: Robert Xu
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2linkedlist(ls):
    head = cur = ListNode(ls[0])
    for i in range(1,len(ls)):
        cur.next = ListNode(ls[i])
        cur = cur.next
    
    return head

def printlinkedlist(head):
    while head:
        print(head.val, end = ' ')
        head = head.next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            carry, val = divmod(a+b+carry, 10)
            cur.next = ListNode(val)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry:
            cur.next = ListNode(1)
        
        return dummy.next

a = Solution()
l1 = list2linkedlist([9,9,9,9,9,9,9])
l2 = list2linkedlist([9,9,9,9])

b = a.addTwoNumbers(l1, l2)

printlinkedlist(b)