#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, suma: int):
        if not root:
            return []
        treeStack = []
        popStack = []
        resultArr = []
        total = 0
        result = []
        cur = root

        while treeStack or cur:
            resultArr.append(cur.val)
            total += cur.val
            if cur.left or cur.right:
                popStack.append(0)
                if cur.right:
                    treeStack.append(cur.right)
                    popStack[-1] += 1
                if cur.left:
                    treeStack.append(cur.left)
                    popStack[-1] += 1
            else:
                if total == suma:
                    result.append(resultArr[:])
                total -= resultArr[-1]
                resultArr.pop()
                if popStack:
                    popStack[-1] -= 1
                while popStack and resultArr and popStack[-1] == 0:
                    popStack.pop()
                    total -= resultArr[-1]
                    resultArr.pop()
                    if popStack:
                        popStack[-1] -= 1

            cur = treeStack.pop() if treeStack else None

        return result

# from collections import deque

# def constructorTree(treeList):
#     stack = deque()
#     tree = TreeNode(treeList[0])
#     cur = tree
#     length = len(treeList)
#     for i in range(1, length, 2):
#         if not cur:
#             continue
#         left = TreeNode(treeList[i]) if length >= i + 1 and treeList[i] else None
#         right = TreeNode(treeList[i + 1]) if length >= i + 2 and treeList[i + 1] else None
#         if left:
#             stack.append(left)
#         if right:
#             stack.append(right)
#         cur.left = left
#         cur.right = right
#         cur = stack.popleft()
#     return tree

# Solution().pathSum(TreeNode(1), 1)
# @lc code=end
