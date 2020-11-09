#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
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

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.dfs(root, None)
        return root
        
    def dfs(self, cur, nextNode):
        if cur is None:
            return None
        cur.next = nextNode
        self.dfs(cur.left, cur.right)
        self.dfs(cur.right, cur.next.left if cur.next else None)
# @lc code=end

