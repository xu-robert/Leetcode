# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:52:08 2020
Number of ways of cutting a pizza

You are given a 2d grid of 'A' (apple) and '.' and an integer k, and asked to find the number of ways you can cut the pizza
so that each piece has at least one 'A'. You can cut the pizza vertically or horizontally. If you cut vertically,
the section to the left of the cut goes to someone. If you cut horizontally, the section above the cut goes to someone.
*You can not cut those pieces given away

This is basically classic dynamic programming. We can make some number of vertical and horizontal cuts which end up
at the same slice of pizza remaining, so there are overlapping subproblems. So here is the idea: first we go from left
to right through the cake (making vertical cuts). If we realize we can make a cut at column j that has at least
one apple on the left slice, we make the cut and recursively solve the problem for the remaining piece. Then we do
that for the next column, until we reach the second last column (no point cutting off from the last column since
there is no pizza remaining). Repeat the process for the rows, and at the same time memoize the solutions for the
subproblems so we don't spend time solving already solved problems.

The trick to getting this to be a fast solution is fast access of knowing whether there is an apple on the left side
of the vertical cut you are about to make, or apple on above the horizontal slice you are about to make. With a bit
of preprocessing, we can do this in O(1) time, using the block sum concept which will easily tell us the sum of
any n by m block of the pizza. If we know that a block contains an apple, we make the slice. So how does this work..

Easy to show by example: the pizza shown below (replace 'A' with 1 and '.' with 0)
 [[1,0,0],
  [1,1,1],
  [1,0,0]]
 
is transformed into a matrix block_sum

[[1,1,1],
 [2,3,4],
 [3,4,5]]

where the (i,j) element in block_sum represents the sum of all elements in the submatrix pizza[0:i][0:j] 
using the formula bs[i][j] = bs[i-1][j] + bs[i][j-1] - bs[i-1][j-1] + pizza[i][j]

Heres how it works: bs[i-1][j] is the block sum of the submatrix pizza[0:i-1][j], likewise for bs[i][j-1]. If we 
add the two of them together, we double count the sum of submatrix pizza[0:i-1][0:j-1], so we subtract it once.
Finally, we add in pizza[i][j]. either 0 or 1, to get the block sum of pizza[0:i][0:j]. The only modification in the
algorith itself is to pad block_sum with 0 on the top and left side, to make for more concise code.

Now, its a bit more difficult to explain how we use this concept to retrieve our block sums in O(1), especially in 
text alone, but I will try. Suppose our original pizza had n rows and m columns, and we are currently solving the 
subproblem with p rows and q columns. 

<------------ m ------------->
[[1, 0, ...                 1] ^
[0, 1, ...                  0] |
.                              | 
.                              n   
.                              |
[0, 0, ...      (p,q)       1] |
.                              |
.                              |
.                              |
[0, 1, ...                  0]]v 

I will just explain how we decide whether or not to make a horizontal cut
since it is essentially the same for a vertical cut. So the boundaries of our current piece is (p, q). starting with
i from p+1 until n-1, I want to determine whether the block pizza[p:i][q:m] contains at least one apple. So what
we need to do is find block sum of pizza[0:i][0:-1] (sum of entire pizza up to row i, equal to block_sum[i][-1])
 and subtract the following blocks: pizza[0:p-1][0:-1] (sum of pizza up to row p-1, or block_sum[p-1][-1]) and
 pizza[0:i][0:q-1] (sum of pizza from row i to column q, or block_sum[i][q-1]). Because we double subtracted region
 block_sum[i-1][j-1], we add it back in once. And that tells us our sum. If its greater than or equal to one, hurray
 we make the slice. Otherwise, we keep increasing i until either we have no more pizza to cut, or we get a slice with
 an apple. Same thing for the columns
 
 Finally, we get to our base case. If k == 1, all we do is check whether or not the remaining piece contains an apple
 if it does, return 1, else 0. I wont go into depth how we query the block sum to get that result, the formula should
 be self explanatory (I hope, otherwise I plan to return to this and make a video)

 
@author: Robert Xu
"""
class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        
        block_sum = [[0 for _ in range(len(pizza[0])+1)] for _ in range(len(pizza)+1)]
        
        dp = {}
        for i in range(1, len(pizza)+1):
            for j in range(1, len(pizza[0])+1):
                block_sum[i][j] = block_sum[i-1][j] + block_sum[i][j-1] - block_sum[i-1][j-1] + (pizza[i-1][j-1] == 'A')
        
        
        def helper(i, j, k):
            
            if (i, j, k) in dp:
                return dp[(i,j,k)]
            
            if k == 1:
                return 0 + (block_sum[-1][-1] - block_sum[-1][j-1] - block_sum[i-1][-1] + block_sum[i-1][j-1] > 0)
            
            res = 0
            for n in range(i, len(pizza)):
                if block_sum[n][-1] - block_sum[i-1][-1] - block_sum[n][j-1] + block_sum[i-1][j-1] > 0:
                    res += helper(n+1, j, k-1)
                    
            for m in range(j, len(pizza[0])):
                if block_sum[-1][m] - block_sum[-1][j-1] - block_sum[i-1][m] + block_sum[i-1][j-1] > 0:
                    res += helper(i, m+1, k-1)
            
            dp[(i,j,k)] = res
            return dp[(i,j,k)]
        
        return helper(1,1,k)

a = Solution()
b = a.ways(pizza =["A..","A..","..."],k=1)