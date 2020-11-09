#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if root is None:
            return []
        result = []
        lvList = deque()
        lvList.append(0)
        treeStack = deque()
        node = None
        treeStack.append(root)
        while len(treeStack) != 0:
            lv = lvList.popleft()
            if lv % 2 == 1:
                node = treeStack.popleft()
            else:
                node = treeStack.pop()
            if len(result) - 1 < lv:
                result.append([])
            result[lv].append(node.val)
            if lv % 2 == 1:
                if node.right:
                    treeStack.append(node.right)
                    lvList.append(lv + 1)
                if node.left:
                    treeStack.append(node.left)
                    lvList.append(lv + 1)
            else:
                if node.left:
                    treeStack.appendleft(node.left)
                    lvList.append(lv + 1)
                if node.right:
                    treeStack.appendleft(node.right)
                    lvList.append(lv + 1)
        return result

# @lc code=end

