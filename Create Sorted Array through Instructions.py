# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 11:23:16 2021
Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:

The number of elements currently in nums that are strictly less than instructions[i].
The number of elements currently in nums that are strictly greater than instructions[i].
For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7

 

Example 1:

Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.
Example 2:

Input: instructions = [1,2,3,6,5,4]
Output: 3
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.
Example 3:

Input: instructions = [1,3,3,3,2,4,2,1,2]
Output: 4
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.
 

Constraints:

1 <= instructions.length <= 105
1 <= instructions[i] <= 105

Solution
I am upset because I spent a lot of time looking for a O(n) solution because the potential input size is so large,
couldn't do it, then I gave up and peeked at discussion to see other solutions time complexity. Turns out all the top
rated solutions were O(nlogn), which I already thought of a solution for, and implemented it in pretty few lines of code.
Oh well! Maybe there is a O(n) or O(max(instructions)) solution, but I am not smart enough to figure it out. 

I never bothered to learn how to implement a fenwick tree, which could solve this in O(nlogn) time as well. Instead, I 
opt here to use a SortedList, which is a data strcuture implemented in python. It maintains a (sorted) list, which
supports ~ O(logn) insertion and search, which is exactly what I need. The relevant methods are add (just add to the list)
and bisect_left/bisect_right, which search for the proper index to insert an element. Bisect left returns the index
at which the element should be inserted ON THE LEFT while bisect right obviously return the appropriate right index.

Bisect_left will coincidentally return the number of elements smaller than the inserted element, while if we know
the length of the sorted list, len-bisect_right(lement) will return the number of elements greater than our inserted
element. Which is exactly what we need!

Essentially, we just iterate through our instructions and add the current element at each iteration. After insertion,
our sortedlist has length i+1 where i is our current index in instructions. As mentioned earlier, we use
bisect_left(instruction[i]) to get the number of strictly smaller elemets, and i+1-bisect_right(element) to get the
number of strictly greater elements. The cost of insertion is the minimum of these two, which we then add to ans.

THe algorithm is a straightforward implementation of the aboce. 
"""

from sortedcontainers import SortedList

class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        sl = SortedList()
        ans = 0
        
        for i in range(len(instructions)):
            
            sl.add(instructions[i])
            
            num_smaller = sl.bisect_left(instructions[i])
            num_greater = i+1 - sl.bisect_right(instructions[i])
            
            ans += min(num_smaller,num_greater)
        
        return ans % (10**9+7)

a = Solution()
b = a.createSortedArray([1,3,3,3,2,4,2,1,2])