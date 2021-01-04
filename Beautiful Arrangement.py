# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 09:56:35 2021
Beautiful Arrangement

THERE IS A PIC FOR THIS SOLUTION

Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15

Solution
Initially I did not see the constraint so I thought this was a dp program. But because n is limited to 15, it makes
sense that the solution might be backtracking somehow. This was a good and much needed refresher on backtracking,
which I haven't used in a while. Here are two solutions: an iterative one and a recursive one. I noticed an important
distinction between the iterative and recursive approach as well. This problem is quite similar to Letter Tile Possibilities

For the iterative approach, I use a shared resource (set of remaining (unused) elements) while doing a postorder 
traversal of a recursion tree. This is my favorite way to solve backtracking problems generally. We dont need to make
any copies of anything, just have the shared resource and keep track of visited states. In this case, our state is
given by the current number, and the set of remaining numbers. The set of remaining numbers implies the position of the
current number. Because we are using the set of remaining numbers as a shared resource, we actually dont need
to keep track of the exact state in the stack: we only store (num, index, visited), but the state of the remaining
pool is updated as we add and remove from it as we traverse the tree.

 We initialize our stack to
[(1,1,False), (2,1,False)... (n, 1, False)]. Each item in the tuple is respectiely: the number, the index where we place
the number, and a visited flag. We initialize our remaining set to contain all (1..n) elements. Then we begin our
traverse.Note that all n numbers can be placed at index 1 because n % 1 == 0 for any positive integer.

First we pop from the stack: num, index, and visited. If our index == n, we have reached a feasible solution by placing
num at index. At this point, the only element of remaining should be num itself. Since we reached a solution, we 
increment our answer and backtrack. Note that index == N is a special case: we dont need to re-add num back into
remaining since we never removed it. 

After that first check, our second check is whether or not we have visited this state: when we see that visited == True,
this means that we have explored all feasible possibilities where we have placed num at index with the current set of
remaining numbers. So we backtrack by adding
num back into the pool of remaining numbers and continue our dfs from the next state. 

Finally, if our visited flag is False, then we need to explore the child possibilities of placing num at index. First
we re add (num, index, True) to the stack. THis will let us know when we have finished exploring all the child 
possibilities of this state. Then
we remove num from the pool of remaining numbers, and then for each n in remaining, we check if we can maintain
a beautiful arrangement by putting n at index + 1. The condition for this is n%(index+1) == 0 or (index+1)%n == 0.
If so, we add that state to the stack, with a visited == False flag. 

I have added a picture for the iterative solution showing how we traverse the dfs tree. Arrow lines show the 
direction in which we traverse, while parent-child node relationships are shown as straight lines. Sometimes we move 
laterally from children to children, and in the case of the first child (leftmost child) of a parent, we move from 
child to parent node. THis is the point we would hit visited == True for the parent node.

For the recursive solution, I tried to code it up the same way: using a global remaining resource and DFS. However,
something bad happens if we try this: the code is shown in countArrangementRecursiveBAD. THe problem is: we
are removing and adding elements from the remaining set AS WE ARE ITERATING IT. Since When I call DFS at a certain point,
the dfs will remove then add elements into the global resource. I think this messes up the iteration process, as
it will repeat iterations for some reason. So this is a lesson to NOT mix global resource where items are being added
and removed, and recursion. Instead, I used a global boolean array to store whether or not an element has been used 
already. This has a penalty on the time complexity, since I need to check all N elements for every time DFS is called,
but we dont have the same problem where the set is altered during iteration. 


@author: Robert Xu
"""
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        remaining = set([i for i in range(1, N+1)])
        
        ans = 0
        
        stack = [(i, 1, False) for i in range(1, N+1)]
        
        while stack:
            
            num, index, visited = stack.pop()
            
            if index == N:
                ans += 1
                continue
            
            if visited == True:
                remaining.add(num)
            
            else:
                stack.append((num, index, True))
                remaining.remove(num)
                for n in remaining:
                    if n%(index+1) == 0 or (index+1)%n == 0:
                        stack.append((n,index+1,False))
        
        return ans
    
    def countArrangementRecursiveBAD(self, N):
        
        remaining = set([i for i in range(1, N+1)])
        
        self.ans = 0
        
        def dfs(index, num):
            
            if index == N:
                self.ans += 1
                return
            
            remaining.remove(num)
            
            for n in remaining:
                if n%(index+1) == 0 or (index+1)%n == 0:
                    dfs(index+1, n)
            
            remaining.add(num)
        
        for x in range(1, N+1):
            dfs(1, x)
        
        return self.ans

    def countArrangementRecursive(self, N):
        
        used = [0]*N
        
        self.ans = 0
        
        def dfs(index, num):
            
            if index == N:
                self.ans += 1
                return
            
            used[num-1] = 1
            
            for n in range(1,N+1):
                if used[n-1] == 0:
                    if n%(index+1) == 0 or (index+1)%n == 0:
                        dfs(index+1, n)
            
            used[num-1] = 0
        
        for x in range(1, N+1):
            dfs(1, x)
        
        return self.ans
a = Solution()
b = a.countArrangementRecursiveBAD(3)