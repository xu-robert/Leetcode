# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:09:53 2020

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Example:

Input: [2,1,5,6,2,3]
Output: 10

Note that a rectangle cannot consist of "empty space", its whole area must consist of histogram bars. Just draw it out
to see why the answer to the above example is 10.

Solution:

THis was a fun and challenging problem. I had a few ideas that I was not confident in until I found the solution that I
like. So I had this problem spoiled before - I read it somewhere in an article about monotonic stacks, so I knew that
the solution would probably use a monotonic stack - but how exactly it should be implemented I had to figure out.

THe first thing I thought of is that for any rectangle in the histogram defined by the range
(i,j), the height of the rectangle is limited by some heights[k] where heights[k] is the minimum of heights[i]..heights[j]
and k is in the range (i,j). So heights[k] is definitely a member of heights[i]..heights[j]. So if we go through
each element of the array and treat the element as k: that is we think of it as the smallest height in a rectangle formed
by heights[i]..heights[k]..heights[j], and we find the largest area of the rectangle where that element is the smallest
height, then one of the elements in the array will be the k with the largeset rectangle. 

For example: we have 2,1,5,6,2,3. We go through each element of the array, starting with k = 0 and h[k] = 2.
What is the largest rectangle we can make where 2 is the smallest height? In this case the answer is just a rectangle
with area = 2, because we have no elements to the left of 0, and the element to the right of 0 is h[1] = 1. We cant extend
a rectangle with height 2 to the right because this is not a proper rectangle by the problem definition since it would
occupy empty space. Ans = 2  

Then we move to k=1,h[k] = 1. In this case, we bound the max height of the rectangle to 1. We can
extend the height 1 to the left since 2 > 1, and we can extend this rectangle to the right by 4 elements (5,6,2,3) since
they are all greater than 1 as well. So by bounding our rectangle height to h[1] = 1, the max rectangle we can make is
1*(1 + 1 + 4) where the 3 elements in parantheses represent: number of elements to the left which 1 can extend, the 
element h[i] itself, and the number of elements to the right which 1 can extend. Ans = 6

Then we go to k=2,h[2] = 5. We cant extend to the left, but we can extend one to the right, but ONLY ONE. since 5 < 6 but
5 > 2, the rectangle with height 5 at k = 2 can have a max rectangle of area 5*(0+1+1) = 10. Ans = 10

And so on...

So to summarize what we can observe: the max rectangle has its height bounded by some h[k]. To find the max rectangle 
made by bounding the rectangle height at h[k], we calculate h[k]*(num_left + 1 + num_right) where num_left is
the number of elements to the left of k where ALL h[i] > h[k], 0 <= i <= k, and similarly for num_right. THe really 
important thing to understand is that we shold be able to draw a straight horizontal line from k to the left and right
sides of k - num_left, k+ num_right with a height of k, and the line should always be within a histogram bar. 

So now the task becomes how to find num_left and num_right for each k. This is where our monotonic stack will be used.
The process is essentially the same for num_left and num_right, except we do one in the reverse direction (num_right).
So I will explain for num_left. Lets use a different example: arr = [1,3,2,2,7,6,2,4,3,1]

We initialize an array left to store num_left, and an empty stack. We iterate the array from left to right, and
at each iteration for arr[i] we determine left[i]. The stack will contain indices of arr, not the values of arr.
The important property is that if arr[i] <= arr[i-1], then left[arr[i]] = 1 + left[arr[i-1]]. That is what allows us
to calculate left in O(n) time

Initially we have stack = [], left = []

Then we have i = 0:
Trivially, we always have left[0] = 0, since there are no elements to the left of 0.
stack = [0]
left = [0]

i = 1
Since arr[i] > arr[stack[-1]] (3 > 1), there are no elements to the left of 3 such that a rectangle of height 3 can 
be formed. left[1] remains at 0
stack = [0,1]
left = [0,0]

i = 2
Now, arr[i] < arr[stack[-1]] (2 < 3), which means that a rectangle of height 2 can be extended to the left. How far
can it be extended? Well we pop the 3 off the stack leaving our stack  = [0]. We now find arr[i] > arr[stack[-1]] (2 < 1)
So we can only extend the height 2 rectangle left by 1 unit (the 3 that was popped). So left[2] = 1. THis means
that any element later on, if it has height <= 2, also is less than 3, so will gain an extra +1 for its left. This
is how we carry num_left forwards. 

stack = [0,2]
left = [0,0,1]

i = 3
2 <= 2, so we can extend our rectangle of height 2 at i = 3 to this one. And sinze left[2] = 1, this indicates
to us that there is another element to the left of i = 2 which is >= 2. So we pick up 1 + 1 left rectangles. We pop
2 from stack and replace with i

stack = [0,3]
left = [0,0,1,2]

i = 4
stack = [0,3,4]
left = [0,0,1,2,0]

i = 5
Now we have 6 < 7, so we pop from stack and left[5] = 1. But we can only pop that one element. Note that when
we pop an element from the stack, we are basically saying it is no longer relevant. All of that elements information
has been absorbed into left[i] of the ith element which popped it. From the moment its popped, we now only care if 
upcoming elements are smaller than the element which popped it: if it is, its info gets passed on.

stack = [0,3,5]
left = [0,0,1,2,0,1]

i = 6
For the first time we are popping multiple elements from the stack: first we have (2 < 6) so we gain 1+left[5] = 1+1 = 2
for left[i]. This corresponds to 2 < 6 < 7. Then we gain 1 + left[3] = 1+2=3 by popping 3. This corresponds to
2 <= 2 <= 2 <= 3. Now i=5 and i=3 are irrelevant. We can only gain the 2+3 = 5 left elements by being less than the
current arr[i] = 2. 

stack = [0,6]
left = [0,0,1,2,0,1,5]


The rest of the problem follows the same pattern. For num_right, we just run the above algorithm of the reversed
array and reverse the result. Why this is should be straightforward (the output of running the reversed array will
                                                                     be in reversed order)

Once we have left and right, we just use our original logic to determine the max area of a rectangle constrained by 
heights[k]: heights[k]*(num_left + 1 + num_right), and take the max out of all k. 


                                                                                                         
@author: Robert Xu
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        def max_side(heights):
            
            arr = [0]*len(heights)
            stack = []
            
            for i in range(len(heights)):
                while stack and heights[i] <= heights[stack[-1]]:
                    arr[i] += 1 + arr[stack.pop()]
                    
                stack.append(i)
            return arr
        
        left = max_side(heights)
        right = max_side(heights[::-1])[::-1]
        
        ans = 0
        for rect, left_num, right_num in zip(heights, left, right):
            ans = max(ans, rect*(left_num + 1 + right_num))
        return ans
    
a = Solution()
b = a.largestRectangleArea([2,1,5,6,2,3])