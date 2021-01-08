# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:02:05 2021
Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.

Solution:
Really easy question, you could use ''.join() and just compare the two strings but I wrote an inplace solution.
We just go element by element, see if equal, if not return false, otherwise continue. Blah Blah

@author: Robert Xu
"""
class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        
        i=j=0
        m=n=0
        
        while i < len(word1) and j < len(word2):
            
            if word1[i][m] != word2[j][n]:
                
                return False
            
            m += 1
            n += 1
            
            if m == len(word1[i]):
                m=0
                i+=1
            
            if n == len(word2[j]):
                n=0
                j+=1
        
        return i == len(word1) and j == len(word2)

a = Solution()
b = a.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"])