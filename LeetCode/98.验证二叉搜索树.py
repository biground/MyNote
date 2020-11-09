#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur = root
        treeStack = []
        result = []
        while cur or treeStack:
            if cur:
                treeStack.append(cur)
                cur = cur.left
            else:
                cur = treeStack.pop()
                if result and cur.val <= result[-1]:
                    return False
                result.append(cur.val)
                cur = cur.right
            
        return True

# @lc code=end
