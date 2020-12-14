# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:03:32 2020

Implement a MyCalendarThree class to store your events. A new event can always be added.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A K-booking happens when K events have some non-empty intersection (ie., there is some time that is common to all K events.)

For each call to the method MyCalendar.book, return an integer K representing the largest integer such that there exists a K-booking in the calendar.

Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)
Example 1:

MyCalendarThree();
MyCalendarThree.book(10, 20); // returns 1
MyCalendarThree.book(50, 60); // returns 1
MyCalendarThree.book(10, 40); // returns 2
MyCalendarThree.book(5, 15); // returns 3
MyCalendarThree.book(5, 10); // returns 3
MyCalendarThree.book(25, 55); // returns 3
Explanation: 
The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
The remaining events cause the maximum K-booking to be only a 3-booking.
Note that the last event locally causes a 2-booking, but the answer is still 3 because
eg. [10, 20), [10, 40), and [5, 15) are still triple booked.
 

Note:

The number of calls to MyCalendarThree.book per test case will be at most 400.
In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].

Solution:
    
Think of it this way: when we add an event, we are basically adding a parentheses to our day

(). If we add an overlapping event, it would look like (()). If we add a non overlapping event,
it looks like ()(). So we just need to count the max open parentheses to get k. So we just
keep a dictionary storing the event start and end values, which we call calendar. At 
calendar[start], we add 1, and at calendar[end] we subtract 1. The of calendar always balances.

So we just iterate through the sorted calendar keys and note the net events started 
(num events started at t - num events ended at t), and keep track of the max. This implementation
is kind of slow because we need to sort the dictionary keys every time we make a call - we could
use a binary search tree to keep the times so that each call is O(n) instead of O(nlogn)
@author: Robert Xu
"""

from collections import defaultdict

class MyCalendarThree(object):

    def __init__(self):
        
        self.calendar = defaultdict(int)
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        self.calendar[start] += 1
        self.calendar[end] -= 1
        
        k = 0
        n = 0
        for st in sorted(self.calendar.keys()):
            n += self.calendar[st]
            k = max(k, n)
        
        return k
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)