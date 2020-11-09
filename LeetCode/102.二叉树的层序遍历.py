#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: TreeNode):
        if root is None:
            return []
        result = []
        treeStack = deque()
        treeStack.append((root, 0))
        while len(treeStack) != 0:
            node, lv = treeStack.popleft()
            if len(result) - 1 < lv:
                result.append([])
            result[lv].append(node.val)
            if node.left:
                treeStack.append((node.left, lv + 1))
            if node.right:
                treeStack.append((node.right, lv + 1))
        return result

# @lc code=end

