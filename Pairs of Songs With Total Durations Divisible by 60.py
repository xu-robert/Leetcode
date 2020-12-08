# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 09:08:03 2020
Pairs of Songs With Total Durations Divisible by 60

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500

Solutio:
This is basically the two sum problem, with a modulo aspect. If we see a song with time t,
we want to see how many songs are there such that (t+n)%60 = 0. The special case if t%60 = 0,
which we split out into an if else block
@author: Robert Xu
"""
from collections import defaultdict
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
        stored = defaultdict(int)
        ans = 0
        for t in time:
            if t%60 != 0:
                ans += stored[60-t%60]
                stored[t%60] += 1
        
            else:
                ans += stored[0]
                stored[0] += 1
                
        return ans

a = Solution()
b = a.numPairsDivisibleBy60([30,20,150,100,40])