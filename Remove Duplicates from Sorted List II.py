# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:53:06 2021
Remove Duplicates from Sorted List II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

Solution:

Not in place (return new list and new nodes)

We create a dummy node: the next node of the dummy points to the head of our new linked list. We maintain one pointer
that points to our current node in the new list: initially this is dummy. We also keep a pointer that advances through
the original linked list. When we find a node that meets our criteria (unduplicated), we make the next field of our 
current node in our new list point to a new node with the value of the node in the original list, then we advance to
next node in both lists. 

To traverse through the original list, we run two nested while loops. The outer loop runs each time we come to a node
with a new value. When this happens, we initiate count to 1 (we have one node of this value).
Next we run the inner loop, which runs until we reach the last node with the same value (this loop would not
run if there is no node with the same value). As the innter loop runs, we increment count each time we see a node with
duplicate value. By the time we exit the inner loop, our fast pointer points to the last node that has the same value
as the node which we pointed to when we entered the inner loop, and our count variable is the number of nodes which
share the same value. If count == 1, this node has a unique value, so we make the next of our cur node in our new list point
to a new ListNode(fast.val), and we say slow = slow.next. Regardless of whether or not we added a new node to the new
list, we should advance fast here - this wil bring us to a node with a new value. 

We run the outer loop until we reach the end of the list, then return dummy.next, the head of our new list. 

@author: Robert Xu
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode()
        
        slow = dummy
        fast = head
        
        while fast:
            count = 1
            while fast and fast.next and fast.val == fast.next.val:
                fast = fast.next
                count += 1
            
            if count == 1:
                slow.next = ListNode(fast.val)
                slow = slow.next
            
            fast = fast.next
        
        return dummy.next
        
ls = [1,1,1,2,3]
head = ListNode()
cur = head

for n in ls:
    cur.next = ListNode(n)
    cur = cur.next

head = head.next

a = Solution()
b = a.deleteDuplicates(head)

while b:
    print(b.val)
    b = b.next