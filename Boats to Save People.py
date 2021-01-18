# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:30:01 2021
Boats to Save People

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

Solution

Greedy solution: sort the people, and then just use two pointers at end and beginning (left and right)
Left points at the lightest person not on a boat yet, and right points at the heaviest person not on a boat yet.
If left and right can go together on a boat, then we put them on the same boat and move left up 1 and right down 1.
Otherwise, right is too heavy to go on a boat with anyone else, so we put right on its own boat. Regardless, we use
one boat each iteration, so we increment ans. When left > right, we terminate as everyone has been allocated a boat.

SO why does greedy work: Well, the current lightest person needs to go on a boat. THe best choice is to put him on a 
boat with the current heaviest person, if possible. Don't really have a proof, but greedy works for this case. 
@author: Robert Xu
"""
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l,r = 0,len(people)-1
        ans = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            ans += 1
        
        return ans
            
a = Solution()
b = a.numRescueBoats(people = [3,5,3,4], limit = 5)