# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 09:34:23 2020
Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104

Solution:
 Just simulate walking up and down the mountain. If the mountain doesnt cover the whole array,
 return false.

First bit simulates walking up, we walk up if arr[i] > arr[i-1]. If we reach a point where this
does not hold, we should check if we are at the end or start of array, in which case its a false
peak. If not, we walk down and if we can no longer walk down, check if we are at the end of the
array.


@author: Robert Xu
"""
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3: 
            return False
        
        i = 1
        
        while i < len(arr) and arr[i] > arr[i-1]:
            i += 1
        
        if i == len(arr) or i==1: return False
        
        while i < len(arr) and arr[i] < arr[i-1]:
            i += 1
        
        if i == len(arr): return True