# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:46:09 2020

Spiral matrix II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Input: n = 3
Output: [[1,2,3],
         [8,9,4],
         [7,6,5]]

Solution
See what happens with case n = 3. The first row of length 3 consists of elements 1,2,3.
Then we go down to and fill 4, 5. Then we go left 2 and fill 6, 7. Then we go up 1 and fill 8,
and right 1 and fill 9. In this case, we fill 3, 2, 2, 1, 1 numbers, while cycling through
down, left, up, right. 

What about n = 4?
The result should be 

[[1, 2, 3, 4], 
 [12, 13, 14, 5],
 [11, 16, 15, 6],
 [10, 9, 8, 7]]

In which case after filling the first row, we go 3D, 3L, 2U, 2R, 1D, 1L. In general then,
we fill the first row then iterate down from d = n-1 to d = 1. For each value of d, we fill
d elements by moving a pointer in the specified direction, which cycles through D,L,U,R. So to
start, (after filling row 0). We keep a pointer to cycle through the direction, starting at D
and moving to next direction each time we fill d elements. After we fill the d elements twice,
we move to d-1. 

@author: Robert Xu
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(1, n+1):
            matrix[0][i-1] = i
        
        dirs = [(1,0),(0,-1),(-1,0),(0,1)]
        dir_idx = 0
        
        cur_i, cur_j = 0, n-1
        cur_num = n
        
        for d in range(n-1,0,-1):
            for _ in range(2):
                di, dj = dirs[dir_idx%4]
                for _ in range(d):
                    cur_i += di
                    cur_j += dj
                    cur_num += 1
                    matrix[cur_i][cur_j] = cur_num
                dir_idx += 1
        
        return matrix

a = Solution()
b = a.generateMatrix(4)
        
        