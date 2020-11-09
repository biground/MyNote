#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root):
        if not root:
            return float('-inf'), 0
        leftMax, left = self.dfs(root.left)
        rightMax, right = self.dfs(root.right)
        leftTotal = left + root.val
        rightTotal = right + root.val
        return max(root.val, max(max(rightMax, rightTotal), max(leftMax, leftTotal))), max(root.val, max(leftTotal, rightTotal))

    def maxPathSum(self, root: TreeNode) -> int:
        return self.dfs(root)[0]

Solution().maxPathSum(
    TreeNode(
        1, TreeNode(2), TreeNode(3)
    )
)
# @lc code=end

