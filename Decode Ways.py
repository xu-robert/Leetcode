# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:36:49 2020
Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).

Solution

This is a constrained version of the problem "Number of Ways to restore array", where our k is bounded to be 26. That is
any number in the restored string must be less than or equal to 26 and greater than or equal to 1. So we just reuse
our code for that problem. Just to be clear: 
    
    range(i,max(-1,i-2),-1) means we go back two elements from i when we can, since we have at most two digits in our
    current number. If we are near the start string, we can only back as far as the zeroth element, hence the max(-1,i-2).

    Also the below code runs in O(n) time and O(n) space. But we only ever use at most the last two elements of dp, since
    our number can be at most two digits. So we can make this run in O(1) space by using a dp of size 2, or alternatively
    just two variables. I'm too lazy to do this however
@author: Robert Xu
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dp = [0]*(len(s))
        
        for i in range(len(s)):
            num = 0
            for j in range(i,max(-1,i-2),-1):
                num += 10**(i-j)*int(s[j])
                if s[j] != '0' and num <= 26:
                    if j == 0: dp[i] += 1
                    else: dp[i] += dp[j-1]
            if dp[i] == 0:
                return 0
        
        return dp[-1]

a = Solution()
b = a.numberOfArrays('1')