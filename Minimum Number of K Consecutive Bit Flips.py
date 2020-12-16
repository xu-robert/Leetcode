# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:53:21 2020
Minimum Number of K Consecutive Bit Flips

In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

 

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
 

Note:

1 <= A.length <= 30000
1 <= K <= A.length

Solution:

Brute force solution (O(nk)) will time out, so needed to find an O(n) solution. I had to take
on faith that the solution is greedy: we iterate the array from left to right, and everytime we 
encounter a 0, we flip the next k elements. However, when we flip the next k elements, its 
possible that there is a 1 somewhere in there, which gets flipped to zero, and requires an
additional flip to return it to 1. So basically we just need to flip everytime we encouter a 0.
If we reach the kth from last element (or kth from last + 1, not sure) and the element is a zero,
we return false, because we can no longer make a k length flip to get rid of the zero.

Why does the greedy approach work? As with all greedy problems, I have no idea. BUt anyways,
the solution: As previously mentioned, the O(nk) solution times out: in that approach, everytime
we encounter a 0, we flip the next k elements, then go to the next element. Why is this
inefficient? Well we are flipping the same bits back and forth in some cases: take for example

[0,1,1,0,1,1,0,0,0] with k = 4.

If we are doing greedy, we see the first zero and flip:
    
[1,0,0,1,1,1,0,0,0]

This causes A[1] to be zero, so when we reach i = 1, we flip again:
    
[1,1,1,0,0,1,0,0,0]

Notice how the the elements at i = 2 and i = 3 get flipped twice just to end at the same
position? This is what we need to address to get an O(n) solution. 

Think about what happens when we flip an element: we also need to flip the next k-1 elements.
So how about we use an array to keep track of when we need to flip back? This way we just
need to track our state until we reach the point when we flip back, at which point we flip our
state. We can be in one of two states: flip (f) or no fliip (nf). The states only transition
back and forth, and we can represent the states using either 0 (nf) or 1 (f). For example:
we see that A[i] is 0 and our current state is nf. Then we need to transition to f, and flip
back to nf after we flip the i+k-1 element. Similarly, if our state is f and A[i] is 1, 
we need to revert our state to nf (otherwise it would get flipped to a zero). Each time we
make such a flip, we increment our answer. Lets use our example [0,1,1,0,1,1,0,0,0] 
but with k = 3

We start with
A = [0,1,1,0,1,1,0,0,0]
F = [0,0,0,0,0,0,0,0,0]
ans = 0
state = nf

We start i = 0, and find that we need to flip our state in order to set it to a 1. Note
that the algorithm does not actually change A, but this would be the new state of A after the flip

A*= [1,0,0,0,1,1,0,0,0] A* is the imaginary state of the array after the flip, A does not change
F = [0,0,1,0,0,0,0,0,0] The 1 at i = 2 (0+3-1) indicates that after we flip that element, we flip our state back
ans = 1
state = f

Then at i = 1 we see A[1] = 1, but because of our last flip, our state is f. Meaning
that if were to remain in f state, we would need to flip the 1 to a 0. So we need to make
another flip to nf state.

A*= [1,1,1,1,1,1,0,0,0]
F = [0,0,1,1,0,0,0,0,0] The 1 at i = 3 indicates that there is a state transition after the i=3 element
ans = 2
state = nf

At i = 2, we see A[2] = 1, which is fine in our current state of nf. Note that A[2] was
flipped twice, leaving it at the original value, and we did not have to actually change it in
the array! However, at i = 2, F[i] == 1: this means that we have an automatic change in
state due to a previous flip wearing off. In this case it is the flip at i = 0. This causes
our state to flip from nf to f, as we still have the effects of the flip at i = 1 in play.

ans = 2
state = f

At i = 3, We see A[3] = 0, and our state is f. This means that the 0 will be flipped to a 1 due
to the effects of previous flips (the flip at i = 1). After this point, because Flips[i] = 1,
the effects of that flip at i = 1 wear off and we transition from f to nf, which is our starting
state. 

ans = 2, 
state = nf

At i = 4, A[4] = 1 and state is nf. We dont need to do anything here, Flips[i] is 0 so there is
no action. Same at i = 5.

At i = 6, we need to flip:
A*= [1,1,1,1,1,1,1,1,1]
F = [0,0,1,1,0,0,0,0,1]
ans = 3
state = f

And thats basically the end! The commented out algorithm is the previoulsy described algorithm,
but we can shorted it by making the following observation: since our state is represented by 1
and 0, and so are the elements, we notice that we only flip if the state == A[i]. I.e. if our
state is 0 (nf) and A[i] is 0, we flip. If our state is 1 (f) and A[i] is 1, we flip. So 
we dont need to make special cases for different states, and combine into a single block. 

@author: Robert Xu
"""
class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        state = 0
        flips = [0]*len(A)
        ans = 0
        for i in range(len(A)):
            
            if A[i] == state:
                
                if i+K > len(A): 
                    return -1
                state = 1 - state
                ans += 1
                flips[i+K-1] = 1
                
            if flips[i]: 
                state = 1 - state
            
            # if state == 0:
            #     if A[i] == 0:
            #         if i+K > len(A): return -1
            #         state = 1
            #         ans += 1
            #         flips[i+K-1] = 1
                    
            # else:
            #     if A[i] == 1:
            #         if i+K > len(A): return -1
            #         state = 0
            #         ans += 1
            #         flips[i+K-1] = 1
            
            # if flips[i]: 
            #     state = 1 - state
                
        return ans
a = Solution()
b = a.minKBitFlips(A = [0,0,0,1,0,1,1,0], K = 3)
    
                    
            