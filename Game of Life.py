"""
Created on Wed Dec 30 09:40:04 2020
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
 

Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

Solution
I implemented the so called "in place" solution: In the first pass, 

For a cell i,j, we iterate its 8 neighbors k,l. If k,l is >0, that means
it (k,l) was a 1 in the last iteration. If board[i][j] > 0, this means that board[i][j] was also 1 in the prebious 
iteration. So we add 1 to board[i][j], meaning that in the prebious iteration, it had board[i][j] - 1 live niehgbors.
On the other hand, if board[k][l] > 0 and board[i][j] <= 0, board[i][j] was dead in the last iteration. For these cases,
we subtract 1 from board[i][j] - thus negative numbers denote that board[i][j] was dead in the last iteration while 
board[i][j] > 0 indicates that it was live in the last iteration. At the end of the first pass, positive board[i][j]
means i,j was a live cell with board[i][j] -1 live neighbors. Negative board[i][j] means i,j was a dead cell with
board[i][j] live neighbors. In the second pass, we just note that there are three cases where the cell would be live
in the next iteration: board[i][j] == 3, board[i][j] == 4 (these are cases where live cell had 2 or 3 live neighbors)
or board[i][j] == -3 (dead cell with 3 live niehgbors). SO we just update board accordingly.

It is very worth mentioning a comment from the discussion:
    
 wouldn't agree with the solution for followup 1, that the space complexity is O(1).

Why? It assumes that the cells are capable of holding integers, and not just True or False bits.
That is a really strong assumption, since why on earth would somebody implement these cells with two state use an extra 7, 15, 31 bit? Of course if somebody really just wasted this much space, than indeed it would be a really silly thing to clone the whole board instead of taking the opportunity.

What if the original board was using True or False bits for representing whether the cell is alive or not? Then this solution is exactly the same of cloning the whole original board, with O(MN) space complexity. Plus it comes with an additional trick (or a headache) that we use that extra bit to create a four state variable to encode the current and the next state of a given cell, and decode in the very next step for updating the next cell. In the memory the two solutions would take the same amount of space:
Approach 1:
board = [... 0, 0, 1 ...]
clone = [... 1, 0, 1 ...]
Program: "Oh we are looking at cell(i,j), let's see clone[i][j] (if we store it row major -> clone_[i*N + j]) and let's update board[i][j]"

Approach 2:
board = [... 01, 00, 11 ...]
Program: "Oh we are looking at cell(i, j), let's see board[i][j][1] to access the original, and let's update board[i][j][0]"

So there are the same amount of information is required: 2MN, it is just the representation that differs: Approach 1 stores it in shape [2, M, N] while Approach 2 stores it in shape [M, N, 2]

hope this helps, because this could be a deal breaker on some interviews

@author: Robert Xu
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                for k in range(max(0,i-1),min(n,i+2)):
                    for l in range(max(0,j-1), min(m, j+2)):
                        if (k,l) != (i,j):
                            if board[k][l] > 0:
                                board[i][j] = board[i][j] + 1 if board[i][j] > 0 else board[i][j] -1
        
        for i in range(n):
            for j in range(m):
                if board[i][j] in (3,4,-3):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
            
        return board
    
a = Solution()
b = a.gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
                