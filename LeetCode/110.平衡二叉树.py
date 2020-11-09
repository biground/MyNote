#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanced(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.balanced(root.left)
        right = self.balanced(root.right)
        if left >= 0 and right >= 0 and abs(left - right) <= 1:
            return max(left, right) + 1
        else:
            return -1
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.balanced(root) >= 0
# @lc code=end

Solution().isBalanced(
    TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
)

