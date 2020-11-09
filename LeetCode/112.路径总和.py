#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right = None):
        self.val = x
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, suma: int) -> bool:
        if not root:
            return False
        treeStack = deque()
        cur = root
        while treeStack or cur:
            lastVal = cur.val
            if cur.left:
                cur.left.val += lastVal
                treeStack.append(cur.left)
            if cur.right:
                cur.right.val += lastVal
                treeStack.append(cur.right)
            if not cur.left and not cur.right:
                if cur.val == suma:
                    return True
            cur = treeStack.popleft() if treeStack else None
        
        return False

# @lc code=end

