"""
Valid permutation for DI sequence

THe straightforward solution is to build the sequence one element at a time, for example for "DID",
we try putting a 0,1,2,3 as the first element, and DFS with the remaining numbers until we find a valid
sequence or we can no longer put a valid number as the next element. I believe this would time out since
if you draw a recursion tree, it looks like you are solving the problem for all subsets, which is not
feasible for large n.

THe key to solving the problem then, is to notice that we don't actuall need to keep track of all the
remaining numbers as we build a sequence. We only need to keep track of how many remaining numbers
are above and below the last number we just added. Depending on whether or not the sequence needs to
increase or decrease, we have different behaviour. Its easier to draw the recursion tree than to explain.

Just use a tuple to indicate (number of elements remaining greater than last number, # elements remaining
                              less than last number). 

Since we are using 2d tuple, we can just use a 2d array to store the bottom up results. 

"""

class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        dp = [[0 for _ in range(len(S)+1)] for _ in range(len(S)+1)]
        
        dp[0][0] = 1
        
        prev_sum = 1
        
        for n in range(1, len(S)+1):
            
            total = 0
            if S[n-1] == 'I':
                x = 0
                
                for i in range(1, n+1):
                    j = n-i
                    x += dp[i-1][j]
                    dp[i][j] = x
                    total += dp[i][j]
                
            elif S[n-1] == 'D':
                total = 0
                
                for i in range(n):
                    j = n-i
                    dp[i][j] = prev_sum
                    prev_sum -= dp[i][j-1]
                    total += dp[i][j]
            
            prev_sum = total
        
        return total % 10**9+7

a = Solution()
b = a.numPermsDISequence("IDDIDIIDD")
                    
                
                
            
            
            
            
            
        
        