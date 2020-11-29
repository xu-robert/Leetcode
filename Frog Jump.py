
"""
403. Frog Jump

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.

Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.

Solution:
    
This is perhaps not optimal, but it gets the job done. Initialize a dictionary with stone location as keys and
an empty set as the vals. In these sets, we will place the possible jumps we can make from this stone. Starting from
stone 0, we can only jump 1. So we add 1 to the set of jumps[1] if it exists, otherwise we can't do anything with 
this jump. Then starting from 1, we can jump either 0,1, or 2. We ignore the 0 jump. This means that we can jump to 2,
and from 2 we can jump 0,1,or 2, or we can jump to 3 and jump 1,2, or 3 from stone 3 (if those stones exist). At each
stone, we iterate over the possible jumps we can make from that stone, either til we reach the target and return
True, or we run out of stones and return False. 

Though this gets the job done, it does not seem like the optimal solution and there are a good chunk that are faster
than this, but i think it is the most straightforward.

"""
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        jumps = {n: set() for n in stones}
        jumps[0] = set([1])
        
        for stone in stones:
            for j in jumps[stone]:
                if stone + j in jumps:
                    if stone + j == stones[-1]: return True
                    
                    for k in range(max(1, j-1),j+2):
                        jumps[stone+j].add(k)
        
        return False
    
a = Solution()
b = a.canCross([i for i in range(1100)])
            
            
            
        
        