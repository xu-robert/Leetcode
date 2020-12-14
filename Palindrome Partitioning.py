# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 09:43:17 2020
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

Not too difficult question but for some reason my solution is super slow, even though
it should not be worse than top rated ones..

Basically we just do backtracking, could do either bfs or dfs. Commented out solution is BFS
using deque. We move one index at a time, identify all the palindromes starting that index, and
add them to our path and add to queue, until index reaches end.

The second solution uses a dp to quickly calculate if substring[i][j] is a palindrome.
The logic here is: if s[i] != s[j], obviously s[i:j] is not a palindrome. If s[i] == s[j],
We have two cases: we could have a short palindrome like 'aa', im which case dp[i][j] true,
or we could have a palindrome like 'abaaba', in which case we check if substring
s[i+1:j-1] is a palindrome. Also we set all dp[i][j] to true.

Then we do a dfs keeping track of our path so far and index, whenever we encounter a palindrome
we append it to path and dfs, after completing the dfs for that palindrome we continue searching
for another palindrome. 
@author: Robert Xu
"""

# from collections import deque

# def is_palindrome(s):
#     i,j = 0, len(s)-1
#     while i <= j:
#         if s[i] != s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True

# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         def is_palindrome(s):
#             i,j = 0, len(s)-1
#             while i <= j:
#                 if s[i] != s[j]:
#                     return False
#                 i += 1
#                 j -= 1
#             return True
        
        # q = deque([[s[0]]])
        
        # index = 1
        
        # while q:
        #     if index == len(s):
        #         return [sub for sub in q if is_palindrome(sub[-1])]
        #     for _ in range(len(q)):
        #         cur = q.popleft()
        #         back = cur.pop()
        #         if is_palindrome(back):
        #             q.append(cur + [back] + [s[index]])
        #         q.append(cur + [back+s[index]])
                
        #     index += 1

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        paldp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for n in range(len(s)):
            for i in range(len(s)-n):
                j=i+n
                if i == j:
                    paldp[i][j] = 1
                elif s[i] == s[j]:
                    if j==i+1:
                        paldp[i][j] = 1
                    else:
                        paldp[i][j] = paldp[i+1][j-1]
                
        ans = []
        def dfs(path, index):
            if index == len(s):
                ans.append(path.copy())
                return
            
            for j in range(index, len(s)):
                if paldp[index][j]:
                    path.append(s[index:j+1])
                    dfs(path, j+1)
                    path.pop()
        
        dfs([],0)
        return ans
            
                

a = Solution()
b = a.partition("aab")