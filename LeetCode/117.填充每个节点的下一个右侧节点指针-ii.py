#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II(链表)
#

# @lc code=start
# """
# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """

class Solution:
    def connectToRight(self, last, nextNode):
        if last is None:
            return nextNode
        if nextNode is not None:
            last.next = nextNode
            return nextNode
        else:
            return last
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        # startPos指向每一层的开头
        startPos = root
        while startPos is not None:
            # dummyNode遍历当前层的所有结点
            dummyNode = startPos
            startPos = None
            # lastNode记录下一层的每一个结点，用于和下一个结点连接
            lastNode = None
            while dummyNode is not None:
                startPos = dummyNode.left if startPos is None and dummyNode.left else startPos
                startPos = dummyNode.right if startPos is None and dummyNode.right else startPos
                lastNode = self.connectToRight(lastNode, dummyNode.left)
                lastNode = self.connectToRight(lastNode, dummyNode.right)
                dummyNode = dummyNode.next
        return root

# @lc code=end

