from typing import List
import random
"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    right.append(num)
                elif num < pivot:
                    left.append(num)
                else:
                    mid.append(num)
            
            if k <= len(right):
                return quick_select(right, k)

            if len(right) + len(mid) < k:
                return quick_select(left, k - len(right) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)