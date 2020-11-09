#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        treeStack = []
        result = []
        tempRoot = root
        LEFT = 1
        RIGHT = 2
        isLeftArr = [LEFT]
        while tempRoot or treeStack:
            if tempRoot:
                treeStack.append(tempRoot)
                if tempRoot and tempRoot.left:
                    isLeftArr.append(LEFT)
                tempRoot = tempRoot.left
            else:
                tempRoot = treeStack.pop()
                direc = isLeftArr.pop()
                result.append((tempRoot.val, direc))
                if tempRoot and tempRoot.right:
                    isLeftArr.append(RIGHT)
                tempRoot = tempRoot.right
        length = len(result)
        if length % 2 == 0:
            return False
        for i in range(length // 2):
            val1, direc1 = result[i]
            val2, direc2 = result[length - i - 1]
            if val1 != val2 or direc1 == direc2:
                return False
        return True
        
# @lc code=end

