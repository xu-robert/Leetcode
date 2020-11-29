# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 09:20:24 2020
Numbers at most N given digit set

Given a set of digits and a number n, how many numbers less than or equal to n can you make with the digit set?
You are allowed to reuse digits.

Unoptimized code here but the central idea is there. Say we have n = 7738 and digits = [1,3,5,7]. Let l = len(digits)
and b = number of digits in n, In this case 4 and 4. First, how many numbers can we build with less than 4 digits?

1 digits: 1,3,5,7 = 4**1 = 4
2 digits: 11, 13,15, 17, 31, 33, 35 ... 77 = 4**2 = 16
3 digits: 111, 113, ...777 = 4**3 = 64

So we can make 4 + 16 + 64 = 84 numbers less than n having 3 or less digits.

Things are a bit more complicated with 4 digit numbers. First of all, we can build all 4 digit numbers that start
with less than 7: ie 1XXX, 3XXX, 5XXX where x can be any element in digits. This is simply 3*4**3 = 3*64 = 192. 
However we can also build a 4 digit number, that starts with 7. 7YYY, where Y cannot be any element of digits.
starting with the second digit: since n is 7738, and we are given that the first digit is 7, the second digits must
also be less than 7. We could have 71XX, 73XX, or 75XX, where X can be anything in digits. In this case we have
3*4**2 = 3*16 = 48. Again, we could also put 7 as the second digit: 77YY. Now the third digit: anything less than 3
we can simply take care of with exponentials like last time: we only have 771X which yields 1*4**1 = 4. We can also place
3 in that digit: now we have 773Y. For the last digit, we use any number less than 8 which gives 7731, 7733, 7735, 7737
= 4*4**0 = 4. So to summarize: 84 numbers less than or equal to 3 digits. 192 numbers with the format 1XXX, 3XXX, 5XXX.
48 numbers with the form 71XX, 73XX, 75XX. 4 numbers with the form 771X. 4 numbers with format 773X. In total: 332.

The pattern we observe is for a number with b digits, we start from the leftmost digit and consider how many number
in our digit set is less than that digit. We use that number and simply exponentiation to calculate the possibilities
of using a digit less than that left most digit to build a b digit number. If that digit is in our digit set, we have
more possibilities to explore by starting the number with that digit. In that case, we move to the second left most
digit and repeat the process. There are two key ideas here: the first is that if we ever reach a digit in n that is
not in our digit set, we calculate the possibilities and terminate. why? Consider if we have n = 6738. The only
possible four digit numbers we have are 1XXX, 3XXX, and 5XXX. We cant start with a 6 since its not in our digit set. If
we encounter this situation, we just break off after calculating. THe second key point is we reach the rightmost digit
in n, and that digit is in our digit set. In that case, since the number specifies less than or EQUAL to n, we need
to add 1 to our final answer. Example: if we have 7735: when we get to the last step, without considering this special
case, we would add 2*4**0 (since there are 2 numbers below 5 and 0 digits to the right of it). But then, we are
missing the fact that we can make 7735. So we just add one in this case. THats all.

@author: Robert Xu
"""
class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        ans = 0
        num_digits = len(str(n))
        digits = [int(x) for x in digits]
        
        for i in range(1, num_digits):
            ans += len(digits)**i
        
        n = str(n)
        num_below = [0]*10
        for i in range(1, 10):
            if i-1 in digits:
                num_below[i] = num_below[i-1]+1
            else:
                num_below[i] = num_below[i-1]
        
        m = num_digits-1
        for i in range(len(n)):
            d = int(n[i])
            if i == len(n)-1:
                ans += (num_below[d]) + (1 if d in digits else 0)
                break
            ans += num_below[d]*(len(digits)**m)
            m -= 1
            if d not in digits: 
                break
            
                
        return ans

a = Solution()
b = a.atMostNGivenDigitSet(["3","4","8"],
44)
        
        
