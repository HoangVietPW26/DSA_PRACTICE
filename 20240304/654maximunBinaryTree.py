from typing import List, Optional
"""
You are given an integer array nums with no duplicates. 
A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: #O(N^2)
    def findMax(self, nums):
            maxVal = 0
            maxPos = 0
            for i in range(len(nums)):
                if nums[i] > maxVal:
                    maxVal = nums[i]
                    maxPos = i
            return maxPos, maxVal

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        if len(nums) == 1:
            return TreeNode(nums[0])
        if len(nums) == 0:
            return

        pos, val = self.findMax(nums)
        tree = TreeNode(val)
        tree.left = self.constructMaximumBinaryTree(nums[:pos])
        tree.right = self.constructMaximumBinaryTree(nums[pos+1:])

        return tree


class Solution: #O(N)
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        nodes = []

        for num in nums:
            node = TreeNode(num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop(-1)
            
            if nodes:
                nodes[-1].right = node

            nodes.append(node)
        return nodes[0]