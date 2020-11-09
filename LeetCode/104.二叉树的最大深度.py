#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 我tm直接层序遍历

from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        level = 1
        tempRoot = root
        treeStack = deque()
        treeStack.append((root, level))
        while len(treeStack) > 0:
            node, level = treeStack.popleft()
            if node.left:
                treeStack.append((node.left, level + 1))
            if node.right:
                treeStack.append((node.right, level + 1))
        return level

# @lc code=end

