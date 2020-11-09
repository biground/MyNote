#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildFromInOrder(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        root = preorder.pop()
        rootNode = TreeNode(root)
        rootPos = inorder.index(root)
        rootNode.left = self.buildFromInOrder(inorder[:rootPos], preorder)
        rootNode.right = self.buildFromInOrder(inorder[rootPos + 1:], preorder)
        return rootNode
    def buildTree(self, preorder, inorder) -> TreeNode:
        return self.buildFromInOrder(inorder, preorder[::-1])

# Solution().buildTree(
#     [1, 2, 3, 4, 6, 5, 7, 9, 8, 10],
#     [2, 1, 6, 4, 3, 7, 9, 5, 10, 8]
# )

# @lc code=end
