#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.calcNode(l1, l2, 0)
    def calcNode(self, l1, l2, flag):
        if l1 is None and l2 is None and flag == 0:
            return None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        val = val1 + val2 + flag
        flag = val // 10
        result = ListNode(val % 10)
        result.next = self.calcNode(l1.next if l1 else None, l2.next if l2 else None, flag)
        return result
# @lc code=end

