# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:38:08 2020
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k. There can be multiple ways to restore the array.

Return the number of possible array that can be printed as a string s using the mentioned program.

The number of ways could be very large so return it modulo 10^9 + 7

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
Example 4:

Input: s = "2020", k = 30
Output: 1
Explanation: The only possible array is [20,20]. [2020] is invalid because 2020 > 30. [2,020] is ivalid because 020 contains leading zeros.
Example 5:

Input: s = "1234567890", k = 90
Output: 34
 

Constraints:

1 <= s.length <= 10^5.
s consists of only digits and doesn't contain leading zeros.
1 <= k <= 10^9.

Solution

This is a nice dp problem. Basically we build a dp array where dp[i] equals the number of 
different numbers <= k we can make with the substring s[:i]. We iterate through s from left
to right, and at each i, we try to find possible numbers under k which end with the digit
s[i]. We use these possible numbers and our dp to add to the number of possible lists we can
make ending at i. Easier to run through an example: lets use s='100203450670' and k = 3000.

Starting with i = 0, s[0] = 1. The only possible number we can make which ends in 1 is 1, since
i is at the beginning of the string. so dp[0] = 1.

i = 1, s[1] = 0. Since we know there are no leading zeroes and the list did not contain 0,
we know that when we encouter a zero, it must be the end of some number. So we iterate backwards
from i, building those potential numbers, or finding out that we cant make any number with that
0 which is less than k. In the latter case, we would find that dp[i] = 0, meaning we have an
invalid input and return 0. In the former case, we can build our number with the following
system. We start with num = 0, and iterate j backwards from i. The max difference between
i and j is the len(str(k)), which is just the number of digits in k. clearly we cant exceed this
otherwise we have built a number bigger than k. Each time we step back from i, we increment
num by s[j]*(10**(i-j)), since we are using base 10 system. For example 323 is 3 + 2*10 + 3*(10**2)
We do this at each j, and if we have build a valid number at s[j], we increment s[i] by dp[j-1].

Few things to unpack there. By valid number, we already stated that num must be <= k. The other 
condition is that s[j] != 0 due to the no leading zero constraint. We will leave the dp[j-1] 
question for later in the example. FOr now, at i = 1, we iterate j until we build 10, which is
the only valid number we can building ending at s[i]. So dp[1] = 1.

i = 2, s[2] = 0. Using similar logic, we can only build 100, so dp[2] = 1.

i = 3, s[3] = 2. Now things are more interesting. We find that we can build two valid numbers
here: 2 and 1002. So there are two ways that a potential list ending at s[3] can end: either
in a 2 or in a 1002. If it ends in 2, then we can just tack a 2 to the end of all the 
valid ways we can restore s[:2] (s[:2] = 100), in other words, dp[j-1]. If it ends in 1002,
well thats the only way it could end. So we get dp[3] = dp[2] + 1 = 2. The two arrays
are [100,2] and [1002]. 

i = 4, s[4] = 0. The only valid num here is 20, leading to dp[4] = dp[2] = 1 ([100, 20])

i = 5, s[5] = 3. Here we can make 3 (j = 5) or 203 (j = 3). dp[5] = dp[4] + dp[2] = 2.

... and so on.

Another edge case that should come to mind here is: what if k < max(s) where max(s) is the 
max value of a single digit in s? Well luckily the algorithm takes care of that for us. If
for example k = 2 and s = 29, when we reach i = 1, and start iterating from j, we will find
that at j = 1, num = 9 and since that is grater than k, we wont add to dp[1]. And because
len(str(k)) == 1, we wont push j any farther, so we end with dp[1] = 0, triggering our terminate
condition. 
@author: Robert Xu
"""
class Solution(object):
    def numberOfArrays(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(str(k))
        dp = [0]*(len(s))
        
        for i in range(len(s)):
            num = 0
            for j in range(i,max(-1,i-n),-1):
                num += 10**(i-j)*int(s[j])
                if s[j] != '0' and num <= k:
                    if j == 0: dp[i] += 1
                    else: dp[i] += dp[j-1]
            if dp[i] == 0:
                return 0
        
        return dp[-1]
                
a = Solution()
b = a.numberOfArrays("1000", 10000)