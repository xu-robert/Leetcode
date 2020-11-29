"""
Maximum Sliding Window

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

Solution:
Interesting question, solve with two concepts: the monotonic stack + double ended queue. 

Combine them by using a monotonic decreasing queue, with queue storing elements in the current window in
decreasing order. Lets look at the example: nums = [1,3,-1,-3,5,3,6,7], k = 3

Lets open up the first window by iterating i until we reach k. Start with an empty queue.
Everytime we reach an element, we consider the window ending at this element. If the element is
bigger than top element of the queue, we pop from queue until our current element is either less than the
top element or the queue is empty. The implication is that if our current element is bigger than the top 
queue element, the top queue element can not be the max in the window (since our window ends at the cur
element. Similarly, if our cur element is less than the top element, our cur element can not be the max
in the window. However, it is a candidate to be the next max when our window slides past the index of 
the current max. To keep track of indices, we append the current number with its index. By the time
we reach i = k in the example, our first window looks like [1,3,-1], and our queue is something like 
[(3, 1), (-1,2)]. The max in the window is 3.

Then we begin sliding our window until the end of the array. Our window begins with i = 0. Every time we
slide the window, we increment i. If i is greater than the index at which our max element occurs 
(queue[0]), then we popleft as it is no longer a candidate for our current max. We repeat the monotonic
stack behaviour for the current element (new right bound of window). After that, whatever element at q[0]
is now the max element of the window. This could either be a) the second max element in the previous
window, which we know to be the second max to the monotonic decreasing nature of the queue, or b) it could
be the new element. If i is less than or equal to the index at which our max element of the previous window
occurs, we dont popleft. We repeat the monotonic part and either a) the max of the current window is the
same as the last window, or b) the current element is larger than the last max. 
    
In the example:

we slide our window to [3,-1,-3]. The just added element, -3, does not pop any elements off the queue.
Our lower bound for the window still contains our last max, 3, so the max for the current window is 3.
Our queue is [(3, 1), (-1,2), (-3,3)]

We slide to [-1,-3,5]. Our lower bound now exceeds the index of our last max so we need to popleft. Our
queue is [(-1,2), (-3,3)]. We consider the current element and it pops off the remaining elements in 
the stack, so that our queue is now [(5, 4)]. the popped elements -1,-3 can never be part of a max 
window containing 5 because any window containing them also contains 5.

etc..

"""

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque([])
        ans = []
        
        for i in range(k):
            while q and nums[i] > q[-1][1]:
                q.pop()
            q.append((i,nums[i]))
        
        ans.append(q[0][1])
        
        i = 0
        for j in range(k, len(nums)):
            i += 1
            if i > q[0][0]:
                q.popleft()
            while q and nums[j] > q[-1][1]:
                q.pop()
            q.append((j,nums[j]))
        
            ans.append(q[0][1])
        return ans
            
                

a = Solution()
b = a.maxSlidingWindow(nums = [4,-2], k = 2)