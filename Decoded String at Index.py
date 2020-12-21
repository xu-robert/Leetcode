# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:21:49 2020
Decoded String at Index


An encoded string S is given.  To find and write the decoded string to a tape, the
encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
 

Constraints:

2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
It's guaranteed that K is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.

Solution:
I was unable to solve this when I first tried months ago, so I looked at the solution back then.
The code I have here is based on what I remembered from that reading, so I could not have solved
this without the looking at the solution ( I believe). SO i feel its a pretty hard question.

What we want to avoid is trying to build the actual decoded string and find the index. This
would take way too much time and memory. So we need to find an easier way. One of the keys to 
understanding this question is how to take advantage of modular arithmetic. Say our
string is a2b3 - our final string is aabaabaab. Notice that we sort of have "fundamental units" 
that make up our string - one is "aab" which is made up of "aa" and "b". If we want to find
the 5th element of aabaabaab, which has length 9, and we know the length of its fundamental unit
"aab" has length of 3, the 5th element is the same as the 5%3 = 2nd element of the fundamental 
unit. Likewise, the 7th element of aabaabaab is the 7%3 = 1st element of aab. Note that
if we want either the 3rd, 6th, or 9th element of aabaabaab, which is b, our previous procedure
would tell us to look at the 3%3, 6%3, and 9%3 = 0 element of the fundamental unit. In this case,
we shold look at the last element of the fundamental unit, which is b.

So if our example is leet2code3, K = 23:

We can easily calculate what the length of the expanded string is, in this case 36.
We note that the last element of S is a 3: that means we have a fundamental unit of 36/3 = 12
repeated 3 times. So finding element 23 in length 36 is equal to finding  23%12 = 9th element
in the unit with 12 length. This corresponds to the problem:
    
leet2code, K = 9. 

In this case, since s does not end with a number, We know that the string must end with "code"
And the elements[0:8] of the decoded string have will not contain "code". So we 
continue to iterate backwards through s, subtracting one from the length of the decoded string
until we either hit another digit or until the length is equal to K.

leet2cod, K = 9, L = 11
leet2co, K= 9, L=10
leet2c, K = 9, L=9: BREAK, return c

If instead our problem was leet2code3, K = 6:
leet2code3, L = 36, K = 6
leet2code, L = 36/3 = 12, K = 6%36 = 6
leet2cod, L = 11, K = 6
leet2co, L=10,K=6
leet2c, L=9,K=6
leet2, L=8,K=6
leet, L=4,K=6%4 = 2
lee,L=3, K=2
le, L = 2, K= 2: RETURN e

or leet2code3, K=8
leet2code3, L = 36, K = 8
leet2code, L = 36/3 = 12, K = 8%36 =8
leet2cod, L = 11, K = 8
leet2co, L=10,K=8
leet2c, L=9,K=8
leet2, L=8,K=8
leet, L=8/2=4,K=8%4=0: RETURN t
@author: Robert Xu
"""

class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        length = 0
        
        for c in S:
            if c.isalpha():
                length += 1
            else:
                length *= int(c)
        
        for i in range(len(S)-1,-1,-1):
            c = S[i]
            if c.isalpha():
                if length == K or K == 0:
                    return c
                length -= 1
            else:
                length /= int(c)
                K %= length
        

a = Solution()
b = a.decodeAtIndex(S = "a2b3c4d5e6f7g8h9", K = 10)