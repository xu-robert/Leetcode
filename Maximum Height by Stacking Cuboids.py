# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 17:03:21 2020
Maximum Height by Stacking Cuboids

Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return the maximum height of the stacked cuboids.

 

Example 1:

(See picture)

Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
Output: 190
Explanation:
Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.
Example 2:

Input: cuboids = [[38,25,45],[76,35,3]]
Output: 76
Explanation:
You can't place any of the cuboids on the other.
We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.
Example 3:

Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
Output: 102
Explanation:
After rearranging the cuboids, you can see that all cuboids have the same dimension.
You can place the 11x7 side down on all cuboids so their heights are 17.
The maximum height of stacked cuboids is 6 * 17 = 102.
 

Constraints:

n == cuboids.length
1 <= n <= 100
1 <= widthi, lengthi, heighti <= 100

Solution

This intuition for the problem is a little tricky, but the code is simple. The key is that we can only stack block A
on top of one block B if ALL block A's dimensions are less than block B's. The problem is that the dimensions depend
on how we rotate a block. For example for a block given by [38,25,45], the width could be 38, 25, or 45, similarly for
the height and length. If we try every combination of rotation and every combination of blocks, this would take far 
too long. 

So then I notice that for a block A, we can only stack it on B if the smallest dimension of block A is <= smallest 
dimension of block B. It sounds like im repeating what I said earlier, but there is a difference. What I am saying is
that if we sort the elements of A (so that [38,25,45] becomes [25,38,45]) and sort the elements of B (so that 
[76,35,3] becomes [3,35,76]), We can only stack A on B if we meet the condition that A[0] <= B[0] and A[1] <= B[1] and
A[2] <= B[2]. If just one of those conditions is false, then there is no combination of A/B rotations such that A
can be stacked on B. So that gives us the idea that we should sort all the individual blocks elements. By doing so,
we can easily tell if block A can be stacked on block B. However, this alone is not enough to solve the problem quickly.
We have dealt with the problem of rotating, but we dont have a way to know which blocks to stack on top of one another.

THe solution to that issue is quite simple: we just sort ALL the blocks in order of their block[0], block[1], and block[2]
elements. In the final sorted list, blocks[j] can NOT be stacked on top of blocks[i], where j > i  because due to 
our sorting, block[j] would have at least one entry > an entry in block[i] (UNLESS all blocks[i] == blocks[j] - key point).

Graphically, after sorting, this is basically saying
[......A.......B.....] we can not stack B on top of A, but we MAYBE could stack A on top of B, if the conditions are met
(B[0] could be >= A[0], but A[1] could be > B[1], in which case A cant be stacked on B).

One last thing before we apply dp: The tallest height we can stack a single block, after sorting, is of course block[-1]
since we sorted by the element of the block. So if we can stack A on B, naturally the talest height is A[-1] + B[-1].
With all these pieces in place, we can proceed with the dp part of the problem.

Lets say A can be stacked on B. Then lets say B can be stacked on C. What is the height of the A-B-C tower? well we
could add A[-1] + B[-1] + C[-1]. OR, we could save the height of the A-B tower and just calculate C[-1] + h[A-B]. This 
is the core of our dp approach. In fact, we don't want to save the height of each X-B tower combintation: we just
want to save the MAX X-B tower combination. so when we find that B can be stacked on C, since we are only interested
in the max height, we just consider the max tower height with B at the base. 

So everything proceeds pretty smoothly from here to get an O(n^2) solution. We do our double sort, then proceed to build
our dp starting from the smallest block (i=0). At each i, we initialize dp[i] = blocks[i][-1], the max height
if our tower contains block[i] only. Then we iterate from j = i-1 down to j = 0. We check if blocks[j] can be stacked
on blocks[i]. If so, dp[i] = max(dp[i], blocks[i][-1] + dp[j] (the max height of a tower with blocks[j] at the base)).
Once we hit j = 0, dp[i] is the max height of a tower with blocks[i] at the base. Then we move to the next i etc..and
updating our ans everytime we reach a new i.


@author: Robert Xu
"""
class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        for cube in cuboids:
            cube.sort()
            
        cuboids.sort(key = lambda x: (x[0],x[1],x[2]))
        
        ans = 0
        
        dp = [0]*len(cuboids)
        
        for i in range(len(cuboids)):
            dp[i] = cuboids[i][-1]
            h = dp[i]
            for j in range(i-1,-1,-1):
                if all(cuboids[i][k] >= cuboids[j][k] for k in range(3)):
                    dp[i] = max(dp[i], h+dp[j])
            
            ans = max(ans, dp[i])
        
        return ans

a = Solution()
b = a.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]])