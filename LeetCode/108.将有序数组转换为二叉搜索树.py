#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def divideConquer(self, nums):
        if not nums:
            return None
        root = nums[len(nums) // 2]
        tree = TreeNode(root)
        tree.left = self.divideConquer(nums[:len(nums) // 2])
        tree.right = self.divideConquer(nums[len(nums) // 2 + 1:])
        return tree
    def sortedArrayToBST(self, nums):
        tree = self.divideConquer(nums)
        return tree

# @lc code=end

