from typing import List
"""
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

"""

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def count(nums, l, r):
            m = l+ (r-l)//2
            if l >= r:
                return 0
            return count(nums, l, m) + count(nums, m+1, r) + count_cross(nums, l, m, r)

        def count_cross(nums, l, m, r):
            
            #1.count
            count = 0
            nL = l
            nR = m+1

            while nL <= m and nR <= r:
                if nums[nL] > 2*nums[nR]:
                    count += (m+1 - nL)
                    nR += 1
                else:
                    nL += 1

            #2. merge
            merge = []
            nL = l
            nR = m+1
            while nL <= m and nR <= r:
                if nums[nL] <= nums[nR]:
                    merge.append(nums[nL])
                    nL += 1
                else:
                    merge.append(nums[nR])
                    nR += 1
            if nL <= m:
                merge.extend(nums[nL:m+1])
            if nR <= r:
                merge.extend(nums[nR: r+1])

            for i in range(l, r+1):
                nums[i] = merge[i-l]
            return count
        l = 0
        r = len(nums)-1

        k = count(nums, l , r)
        print(nums)
        return k
        