#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历(迭代)
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        operationStack = []
        resultList = []
        tempRoot = root
        while operationStack or tempRoot:
            if tempRoot:
                operationStack.append(tempRoot)
                tempRoot = tempRoot.left
            else:
                tempRoot = operationStack.pop()
                resultList.append(tempRoot.val)
                tempRoot = tempRoot.right
        return resultList

# A3 = TreeNode(2)
# A2 = TreeNode(1, A3)
# A1 = TreeNode(3, A2)

# Solution().inorderTraversal(A1)
# @lc code=end

