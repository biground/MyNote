#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildFromInOrder(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = postorder.pop()
        rootNode = TreeNode(root)
        rootPos = inorder.index(root)
        rootNode.right = self.buildFromInOrder(inorder[rootPos + 1:], postorder)
        rootNode.left = self.buildFromInOrder(inorder[:rootPos], postorder)
        return rootNode
    def buildTree(self, inorder, postorder) -> TreeNode:
        return self.buildFromInOrder(inorder, postorder)

# @lc code=end

