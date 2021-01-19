# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 10:47:58 2021
Count Sorted Vowel Strings

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50 

Solution

This is similar to paint houses. Essentially, the solution to n depends on the solution to n-1. The base case is n = 1.
In which case we have 5 strings: a, e, i, o, u. Now for n = 2, what we notice is that only one string can end with a: 
"aa". 2 strings can end with e: "ae" and "ee", 3 can end with i: "ai", "ei", and "ii" et cetera.

so if we represent the number of strings which end with a specific letter with length n as follows:

[a,e,i,o,u]

Then for n = 1 we have

[1,1,1,1,1]

n = 2:
    
[1,2,3,4,5]

and we would find for n = 3:
    
[1,3,6,10,15]

So the pattern is quite simple:
    
for iteration n, cur[1] = 1 and cur[i] = cur[i] + cur[i-1]

for example for n = 2

cur[1] = 1
cur[2] = 1 + cur[1] = 2
cur[3] = 1 + cur[2] = 3
cur[4] = 1 + cur[3] = 4
cur[5] = 1 + cur[4] = 5

and n = 3
cur[1] = 1
cur[2] = 2 + cur[1] = 3
cur[3] = 3 + cur[2] = 6
and so on..

At the end, we just sum cur and get our answer.

The previous solution takes O(n) time. There is however, an O(1) solution which relies on knowing about sequences.
FIrst of all, lets write all the cur's  up to n = 5 or so like the following:
    
[
 [1,1,1,1,1]
 [1,2,3,4,5]
 [1,3,6,10,15]
 [1,4,10,20,35]
 [1,5,15,35,70]
 ]

In particular, lets look at the columns.

For the first column, that is strings ending in "a", no matter what n is, we will have onlt 1 string ending in "a".
For the second column, strings ending in "e", we actually have n strings ending in "e".
The sequence 1,2,3,4,5..is an example of an arithmetic sequence: the difference between terms is a constant. 
We can express the terms of an arithmetic sequence with Tn = an + b. In this case, a = 1 and b = 0

THings get more complicated for the remaining columns.

the "i" column goes like 1,3,6,10,15. Lets look at the differences between terms: the first difference is defined
as the difference between terms in the base sequence. In this case, the first differences go like

2,3,4,5

The second differences are defined as the difference between terms of the first difference (fun right?). In this case
the second differences go like

1,1,1

THe important thing to notice is that the first difference follows an ARITHMETIC sequence. This is known as a quadratic
sequence, and its terms can be expressed as Tn = an^2 + bn + c. If we can solve for a,b, and c, we can predict in 
O(1) time what the nth term of the sequence would be. If we can do this for the fourth and fifth columns, then we ares
set.

So lets run through solving for a, b, and c. Considering we have three unknowns, a system of three equations should
work for us. We already have one of these equations: recall that we have the form Tn = an^2 + bn + c. Well we know
that the 1st term of the sequence is 1, so lets write T1 = 1 = a(1^2) + b(1) + c. SImplifying down to

1 = a + b + c (1)

For equation two and three, we need to derive the equations for a few other terms in the series. Similarly to how
we did T1, we have:

T2 = 3 = 4a + 2b + c (2)
T3 = 6 = 9a + 3b + c (3)

We can diectly solve this system of equations to get a = 1/2, b = 1/2, and c = 0. So, to find the nth element of
our quadratic sequence given by 1,3,6,10.. we can just use Tn = (1/2)n^2 + (1/2)n. Neat right?

So for the "o" column you can probably guess how this is going to go.
The first difference of the sequence 1,4,10,20,35 is 3,6,10,15: the quadratic sequence. If this is the case, we have 
a cubic sequence and you guessed it - Tn can be expressed as an cubic equation: Tn = an^3 + bn^2 + cn + d.

We can use the first 4 terms of the sequence to solve for the coefficients

ANd repeat for the "u" column. That is all! I leave the derivation of the coefficients for whoever is reading - but
its as simple as plugging in n into Tn for the number of equations you need, then solving the system. The restuls are
in the second function: countVowelStringsII.

We can't use 
@author: Robert Xu
"""
class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = [1,1,1,1,1]
        
        for _ in range(1, n):
            for i in range(1,len(cur)):
                cur[i] += cur[i-1]
        
        return sum(cur)
    
    def countVowelStringsII(self, n):
        
        P1 = 1
        P2 = n
        P3 = round(n**2/2 + n/2)
        P4 = round(n**3/6 + n**2/2 + n/3)
        P5 = round(n**4/24 + n**3/4 + 11*(n**2)/24 + n/4)
        
        return P1 + P2 + P3 + P4 + P5
    
a = Solution()
b = a.countVowelStrings(8)
            