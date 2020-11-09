#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root):
        if root is None:
            return None
        treeStack = deque()
        treeStack.append((root, 0))
        lastNode = root
        lastLevel = -1
        while len(treeStack) != 0:
            node, lv = treeStack.popleft()
            if lastLevel == lv:
                lastNode.next = node
            else:
                lastNode.next = None
            lastNode = node
            lastLevel = lv
            if node.left:
                treeStack.append((node.left, lv + 1))
            if node.right:
                treeStack.append((node.right, lv + 1))
        return root

        
# @lc code=end

