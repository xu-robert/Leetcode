# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:14:12 2020
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal
 order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Since the picture does not copy, please draw out the matrix and see how you would reach the output going diagonally from
top left corner to bottom right corner.

Solution:
    
BEcause of all the grid like questions I have come across, I know that each diagonal in a matrix is associated with
a number: see below

THESE ARE the coordinates
[
 [(0,0),(0,1),(0,2)]
 [(1,0),(1,1),(1,2)]
 [(2,0),(2,1),(2,2)]
 [(3,0),(3,1),(3,2)]
 [(4,0),(4,1),(4,2)]
 ]

And note that if we add i and j for every coordinate, we get this:

[
 [0,1,2]
 [1,2,3]
 [2,3,4]
 [3,4,5]
 [4,5,6]
 ]

Each diagonal is associated with a particular i+j sum: We can refer to the nth diagonal as all elements in the matrix
such that i+j=n. In total there are len(matrix) + len(matrix[0]) - 1 diagonals: here we have 3+5-1 = 7 diagonals
with an associated i+j ranging from 0 to 6.

So here is the idea:  We iterate through these diagonals from 0 to 6, starting from the top right
corner of the diagonal and moving to the bottom left. As we iterate, we add these elements to a buffer. Once we reach
the bottom left of the diagonal, our buffer should contain all the elements of the nth diagonal. At this point, we need
to add the elements of the buffer to our answer. If n is even, we add them in reverse order. Otherwise, we add them in 
normal order.

So the only thing we really need to figure out is where the top right corner of the nth diagonal is. The top right corner
is given by coordinate (i,j) where i+j=n. So we know what n is, meaning we only need to know one of i or j as
j = n-i and i = n-j. Lets pick i. Notice that in our example, for the first 3 diagonals, i starts at 0. Afterwards,
i ranges from 1 to 4. Also note that the the 3 diagonals where i starts at 0 corresponds to the number of columns we have
len(matrix[0]). So we can make the following observation: while n <= len(matrix[0]-1), the top right corner of the nth 
diagonal is given by (0,n-i). Once n >= len(matrix[0]), the top right corner of the nth diagonal is given by
(n-len(matrix[0]+1), len(matrix[0])). More generally, we can say that for any n, the top right corner has i coordinate
max(0, n-len(matrix[0])-1), and j=n-i. Once we have i and j, we proceed to move down and left: i += 1, j -= 1, until
we reach other the left edge (j=0) or the bottom edge (i=len(matrix)-1). Once we hit either, the buffer contains all
elements of the nth diagonal. 

@author: Robert Xu
"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        
        for n in range(len(matrix) + len(matrix[0]) - 1):
            
            buffer = []
            
            i = max(0, n-len(matrix[0])+1)
            j = n-i
            
            while i<len(matrix) and j>=0:
                
                buffer.append(matrix[i][j])
                i += 1
                j -= 1
            
            if n%2==0:
                ans.extend(buffer[::-1])
            else:
                ans.extend(buffer)
        
        return ans

a = Solution()
b = a.findDiagonalOrder([[1],[2]])