# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:33:21 2020

Next Greater Element III

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the 
integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it 
does not fit in 32-bit integer, return -1.


Input: n = 12
Output: 21

Input: n = 21
Output: -1

Input: n = 230241
Output: 230412

Constraints:

1 <= n <= 2^31 - 1

This was quite an annoying problem, and I remember looking at the solution before. But I did not look at any solution
when I solved it this time.

First we can handle the special case: when to return -1. We return -1 if there is no number using the same digits of
n such that it is greater than n. THe only time we have this is if the digits are sorted in reverse order already:
a number like 321 or 44331. No matter how we swap the digits around, we can't get a bigger number. We can use this
idea as part of our solution. Take a number like 230241. The answer is 230412. Notice how the first 3 digits remain the
same. If you try this with a lot of numbers, you will find that most likely, we are changing the digits  i:j of n
while leaving 0:i intact. So what is so special about this i and how do we find it? 

Well remember that if digits are sorted in reverse order then we dont have an answer. Similarly, if we find a digit which
violates the sorting order, then we DO have an answer. Lets look at a case like 53862, where the answer is 56238.
Lets iterate through the number in a reversed fasion. First we see 2, then we see 62, then we see 862. So far,
every digit is smaller than the digit to the right of it. But then we see 3862, which violates the sorting we just 
observed for the prvious 3 digits. This occurs at i=1 (left to right). And this tells us that there is at least one
digit n[j] in range(i+1, len(num)) such that n[j] greater than n[i]. Also, by i is the largest i (left to right) such
that it can be replaced with another digit to get the next greater number. i cannot be any further right as all digits
to the right of i are reverse sorted. Eg in our example, 2, 62, and 862 could not be arranged to get a bigger number.
The first - and therefore minimum digit - occurs at i = 1. Note that we could make a bigger number swapping the digit
at i = 0 - but thats not the next greater number.

So we have identified that at i =1, n[i] = 3, will be the best location to replace with a different digit. To get the
next greatest number, this should be the smallest number n[j] in range(i+1, len(num)) such that n[j] > 3. In this
case that number is 6. 8 is also greater than 3, but clearly we get a smaller number if we use the 6 instead of the 8.
So we swap the 3 for the 6 and end up with 56832 - but we are not done yet. Because now 832 is not the smallest number
we can make with the digits 8,3,2, and therefore 56832 is not the smallest number after 53862. To get the smallest,
all we do is sort 8,3,2 to get 2,3,8 or 238 and add that to 56 - to get 56238.

So the steps are:
    
53862

find i where num[i] < num[i+1]
i = 1

find j in range(i+1, len(num)) such that num[j] is greater than num[i] and num[j] is the smallest in that range
to meet the condition
j = 3

swap num[i] and num[j]
56832

concatenate num[:i+1] and sorted(num[i+1:])
56238

Return if our new num is less than 2^32-1 else -1

With some casting between int and str and list where necessary
@author: Robert Xu
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        num = list(str(n))
        
        for i in range(len(num)-2,-1,-1):
            if num[i] < num[i+1]:
                j = i+1
                while j+1 < len(num) and num[j+1] > num[i]:
                    j += 1
                
                num[i], num[j] = num[j], num[i]
                ans = int(''.join(num[:i+1] + sorted(num[i+1:])))
                return ans if ans < 2147483647 else -1
            
        return -1

a = Solution()
b = a.nextGreaterElement(12)