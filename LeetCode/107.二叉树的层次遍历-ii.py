#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if root is None:
            return []
        result = deque()
        treeStack = deque()
        treeStack.append((root, 0))
        while len(treeStack) != 0:
            node, lv = treeStack.popleft()
            if len(result) - 1 < lv:
                result.appendleft([])
            result[-lv - 1].append(node.val)
            if node.left:
                treeStack.append((node.left, lv + 1))
            if node.right:
                treeStack.append((node.right, lv + 1))
        return list(result)

# @lc code=end

