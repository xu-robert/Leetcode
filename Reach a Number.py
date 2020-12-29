# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:49:10 2020
Reach a Number

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].

Solution:

The first thoughts I have are: given the large range of target, BFS will take too long. Also, due to symmetry, the
solution for -target is the same as target.

Here is how I approached the problem:
for a sequence of length n, we know that the sum of the sequence follows some pattern of:
_1 _2 _3 _4 ..... _n, where we fill in the blank with either + or -. For example, -1 + 2 - 3 +4 + 5 = 7. 
The absolute sum of the sequence (if all _ are +) is given by n(n+1)/2 
(sum for an arithmetic sequence starting at 1 ending at n with a difference
of 1 between elements). Lets call this sum t. Now lets group the elemtns in our sequence such that x represents the
sum of all the elements with a (+) in front (sum of positive elements) and y is the sum of negative elements. Then,
we can see that x - y = t. In addition, for a valid sequence, we should have x + y = target. Therefore,
the problem boils down to finding the smallest length of sequence n such that

x - y = t and x + y = target. So one option is to iterate n from 1 to infinity and stop once we find a valid x and y
for that n. Lets try that approach. First, we simplify our equations: add the two to cancel out y and we have

2x = t + target

This will be the crucial formula for us. It tells us two things: first of all, since x is the sum of
positive integers, x itself must be a positive integer. Therefore, the expression (t + target)/2 must be an integer
for a valid n length sequence. In other words, (t+target)%2 must equal 0. Second of all, we have a size constraint.
We know that x is composed of the positive elements of our n length sequence, which has an absolute sum of t. So t >= x
for a valid sequence, which constraints (t + target) / 2 = x <= t.

If these two conditions are met for my n length sequence, I claim that I can make target by splitting n into some
group of positives x, and negatives y, so that x-y = t and x+y = target. Lets use our example of target = 7 with 
5-length sequence. I want to show that _ 1 _2 _3 _4 _5 = 7. Here I have t = 15, and target = 7. So I want to have

x - y = 15 and x + y = 7 ----> 2x = 22 and x = 11. So really, what I need to prove is that for x = integer and x <= t,
I can make any x by taking the sum of a subset of positive numbers in our n length sequence. I want to show that I can make
11 with some combination of 1,2,3,4,5. We can prove that this is always possible with induction: lets say that in this
case that we have proven we can make all elements (1..10) with elements (1,2,3,4). Now I just need to show I can make
(11..15) with some combination of (1,2,3,4,5). Well 1+2+3+4+5 = 15. If I leave out 1, I get 2+3+4+5 = 14. If I leave out
2, I get 1+3+4+5 = 13.. and so on. So by induction, for an n length sequence, You can always make any number <= n(n+1)/2
with some subset of the elements. This is why If we find a valid x for n length sequence, we meet the condition for
a solution.

So the algorithm is really quite simple: take the absolute value of the target, and initialize n = 1 and t = 1. As
we increment n (sequence length) we adjust our t accordingly. If we find that our conditions are met at n = n, we 
return n


So I think we can make this a lot faster if we observe that a lot of the time lost in the above algorith is just waiting
to meet the second condition: target + t //2 <= t. Obviously if our target is 100000000, we dont need to bother checking
the really short sequences like _1 _2 _3, _1 _2 _3 _4. If we can find a lower bound for n, we can skip all these short
sequences.

We can actually do this (find the lower bound) using our formula for t: recall that t = n*(n+1)/2. What we want
to do is find our initial n such that n*(n+1)/2 is very close to the target: this way we skip all the short sequences
which have no chance of adding up to target. So What we do is: set target = n*(n+1)/2. We obtain a quadratic equation
by expanding this all out: n**2 + n - 2*target = 0. Using the quadratic formula, we get n = 0.5*(-1 +- sqrt(1+8*target)).
Of course we only want to keep the positive root: n = 0.5*(-1 + sqrt(1+8t)). We round it down just to be safe,
and recalculate t - this n and t are our starting points - the algorithm is much much faster for large numbers than 
solution 1: I'm pretty sure it also runs in ~ O(1) time because of the following property: once we find that our n 
is sufficiently large, the only condition we need to check is whether or not (t + target)%2 == 0. Well depending on
n, the value of t never stays odd for very for long: since every other number is odd, eventually t will either flip
back between odd and even, which means t + target also flips between even and odd. My hunch is that within 4 increments
of n, t + target will be even somewhere. It does pass all the test cases, so I think it works: In other words, we
dont need a while loop: we can just use a for loop once we find sufficiently large n. 

@author: Robert Xu
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        
        n = 1
        t = 1
        

        while True:
            if (target+t)%2==0 and (target+t)//2 <= t:
                return n
            n += 1
            t += n

class SolutionII(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        
        n = int((-1 + (1+8*target)**0.5)/2)
        t = n*(n+1)//2
        
        # while True:
        #     if (target+t)%2==0 and (target+t)//2 <= t:
        #         return n
        #     n += 1
        #     t += n

        for _ in range(4):
            if (target+t)%2==0 and (target+t)//2 <= t:
                return n
            n += 1
            t += n
        
        return 'pog'
a = Solution()
b = a.reachNumber(7)