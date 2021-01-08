# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 09:57:44 2021

Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Solution

There are two different ways I have solved this problem: one with a sliding window, one with a "jumping" window.

The time complexity of both is O(n) but the jumping window one would be faster. First, the sliding window approach
is classic sliding window. We keep a dict of character counts, a left pointer i (left side of window) and
 then iterate through the string using a pointer j (right side of window). At each
character increment the character count. The moment we see that a character at s[j] is repeated (count > 1),
 we start contracting our window (i+1), until the count of this caracter reaches 1 again. When we found count[s[j]] > 1,
 we are sure that s[j] is the first repeated character: so by the time we contract the window and count[s[j]] = 1 again,
 we are still sure that no characters between the new i and j occur more than once. As we shrink the window, we update
 the counts as well: by decrementing the count of s[i] each time we increment i. At each step of j (increase right window)
 we evaluate max (ans, j-i+1), where j-i+1 is the size of the max valid window ending at j.
 
The motivation for the second approach is that we can get a speed up by not using the while loop in the first solution,
which would take O(2n) time to run. Because in the while loop, all we are doing is incrementing i until we pass the
last index at which s[j] occurred. So, if we store the last index of s[j], we can essentially "jump" our window to the
correct spot rather than incrementing i until we hit it.
 
The second approach also uses a dict, but instead of keeping counts, we keep the last index at which the key appeared. 
We still keep a left side of window i and iterate through array using j to point to right side of window. We initialize
i = 0. Initially since all the elements are unique, we put their indexes into our dict. Then, if there is a duplicate at
j, we will find, in general, that s[j] is in dict AND dict[s[j]] >= i (the last index at which s[j] appeared is greater
than the left side of the window - meaning that we have a duplicate of s[j] in the window). When we find that this is the
case, we can "jump" the left side of the window to i+1: now the window only contains one occurence of s[j]. Note that the
dict[s[j]] >= i is very important: it can be shown by an example: 'kpwwpek'

We shall jump ahead throgu the states where each s[j] has not been seen yet - say we are just finishing j = 2

dict = {k:0,p:1,w:2}, i = 0, ans = j-i+1 = 3.

Then we have j = 3
Here s[j] = 'w', which has been seen before (is in dict) AND dict['w'] = 2 >= 0. So we have a duplicate IN THE WINDOW.
So we jump i to 2+1 = 3, which is now the left side of the max window containing the 'w' at j=3. 
dict = {k:0,p:1,w:3}, i = 3, ans = 3

Next, j = 4
Here s[j] = 'p', which has been seen before, BUT dict['p'] = 1 < i (i=3). So, we have a duplicate in the STRING, but
NOT THE WINDOW. The last occurence of p is outside the current window, so we dont need to contract the window to include
the 'p'. Instead, we just update the dict entry of p to reflect the fact that there is now a 'p' inside the window.
so we have dict = {k:0,p:4,w:3}, i = 3, ans = 3.

j = 5
We have a new element 'e' which we have not seen before. This means we can fit it in the current window without.
dict = {k:0,p:4,w:3,e:5}, i=3,ans=3.

j=6
Same as when j = 4, we have seen 'k' before but its last index is OUTSIDE the CURRENT WINDOW. So we CAN fit it inside
the current window, no contraction needed. We end with
dict = {k:6,p:4,w:3,e:5}, i=3, ans = 4.


@author: Robert Xu
"""

from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringI(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        ans = 0
        counts = defaultdict(int)
        
        for j in range(len(s)):
            counts[s[j]] += 1
            
            while counts[s[j]] > 1:
                counts[s[i]] -= 1
                i += 1
        
            ans = max(ans, j-i+1)
        
        return ans

    def lengthOfLongestSubstringII(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = 0
        ans = 0
        ind_dict = {}
        
        for j, c in enumerate(s):
            if c in ind_dict and ind_dict[c] >= i:
                i = ind_dict[c]+1
            
            ind_dict[c] = j
            ans = max(ans, j-i+1)
        
        return ans
