# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:08:15 2020
Jump game III

Could do DFS or BFS. Track the visited elements and dont visit them again. When you reach 0, return True
if we reach all elements, return False. COuld do inplace as well (mark visited by flipping the sign)

@author: Robert Xu
"""
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        stack = [start]
        visited = set(stack)
        
        while stack:
            cur = stack.pop()
            if arr[cur] == 0:
                return True
            
            if cur + arr[cur] < len(arr) and cur+ arr[cur] not in visited:
                stack.append(cur + arr[cur])
                visited.add(cur + arr[cur])
            
            if cur - arr[cur] >= 0 and cur - arr[cur] not in visited:
                stack.append(cur - arr[cur])
                visited.add(cur - arr[cur])
        
        return False