# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 09:23:09 2021

Longest palindroomic substring

For each index i in the string, we check the longest even length and odd length palindrome that can be formed with
s[i] at the center. For an odd length substring, the center is unique: p[center-1] == p[center+1] but neither = p[center].
For an even length palindrome, the center is not unique. If we treat s[i] as the center, then an even length substring
should have s[i-1] == s[i]. So basically, if we have baabcd, and we are at index i = 1, we start our even length substring
by comparing low = "b" and high = "a". If this condition is met, then we can expand our palindrome: otherwise we terminate.


@author: Robert Xu
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        start = 0
        
        for i in range(len(s)):
            
            low = i-1
            high = i
            
            #even length
            cur = 0
            while low >= 0 and high < len(s) and s[low] == s[high]:
                cur += 2
                if cur > max_len:
                    max_len = cur
                    start = low
                high += 1
                low -= 1
            
            #odd length
            low = i-1
            high = i+1
            cur = 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                cur += 2
                if cur > max_len:
                    max_len = cur
                    start = low
                high += 1
                low -= 1
                
        return s[start:start+max_len]

a = Solution()
b = a.longestPalindrome('ac')