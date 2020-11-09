#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        rightNodeRecordList = []
        nowNode = root
        while rightNodeRecordList or nowNode:
            # 将右子树推入栈中
            if nowNode.right:
                rightNodeRecordList.append(nowNode.right)
            # 将左子树移动到右子树上
            if nowNode.left:
                nowNode.right = nowNode.left
                nowNode.left = None
            elif rightNodeRecordList:
                right = rightNodeRecordList.pop()
                nowNode.right = right
            nowNode = nowNode.right

# @lc code=end

