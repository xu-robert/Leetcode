# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 10:09:13 2020

Jump Game IV

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
 

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8

Solution

Its a fairly straightforward BFS problem if you are familiar with BFS. So for each element in arr,
not only can we go one left or one right, we can also teleport to any other element with the same value.

So first we build that "teleport" graph. We just use a hashmap to store the indices of each unique element.

Then we just do our normal BFS. We start at 0, and visited contains 0. Then we visit left, visit right, and add
left and right indices to visited. Note that when we add right nodes, I didn't include a check to see if right is 
out of array bounds. This is because the only time this would happen is if cur is the last element of arr, which is 
our target index. If we reached that, then we would return already before we get to adding the right index.
After we add right and left, we consider the "teleport" graph. We add all the indices we can teleport to, then remove
the element from the graph because we never need to visit that element again. 

After all that, we increment step by 1: we have visited all the nodes possible at the current step. 

Once we reach the last index, we just return the current step. 

@author: Robert Xu
"""
from collections import deque, defaultdict

class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        positions = defaultdict(list)
        
        for i, num in enumerate(arr):
            positions[num].append(i)
        
        visited = set([0])
        
        q = deque([0])
        
        steps = 0
        while q:
            
            for _ in range(len(q)):
                
                cur = q.popleft()
                if cur == len(arr)-1:
                    return steps
                
                if cur+1 not in visited:
                    q.append(cur+1)
                    visited.add(cur+1)
                
                if cur-1 > 0 and cur-1 not in visited:
                    q.append(cur-1)
                    visited.add(cur-1)
                
                if arr[cur] in positions:
                    for pos in positions[arr[cur]]:
                        if pos not in visited:
                            q.append(pos)
                            visited.add(pos)
                
                    positions.pop(arr[cur])
            steps += 1
            
                
        
a = Solution()
b = a.minJumps([11,22,7,7,7,7,7,7,7,22,13])