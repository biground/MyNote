#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# import copy
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        operationStackP, operationStackQ = [], []
        tempP = p
        tempQ = q
        while tempP or tempQ or operationStackP or operationStackQ:
            if (tempP and (tempQ is None)) or ((tempP is None) and tempQ):
                return False
            if tempP and tempQ and tempP.val != tempQ.val:
                return False
            elif tempP or tempQ:
                operationStackP.append(tempP)
                operationStackQ.append(tempQ)
                tempP = tempP.left if tempP else None
                tempQ = tempQ.left if tempQ else None
            else:
                tempP = operationStackP.pop().right if operationStackP and len(operationStackP) > 0 else None
                tempQ = operationStackQ.pop().right if operationStackQ and len(operationStackQ) > 0 else None
        return True

# @lc code=end

