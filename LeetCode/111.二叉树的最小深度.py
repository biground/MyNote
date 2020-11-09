#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcDepth(self, root) -> int:
        if not root:
            return 1
        left = self.calcDepth(root.left)
        right = self.calcDepth(root.right)
        return min(left if left > 1 else right, right if right > 1 else left) + 1
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.calcDepth(root.left)
        right = self.calcDepth(root.right)
        return min(left if left > 1 else right, right if right > 1 else left)

# @lc code=end

