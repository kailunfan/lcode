#
# @lc app=leetcode.cn id=445 lang=python
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (57.24%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    40.8K
# Total Submissions: 71.1K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
# 进阶：
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
#
#
# 示例：
#
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while s1 or s2 or carry:
            ans = carry
            if s1:
                ans += s1.pop()
            if s2:
                ans += s2.pop()
            carry, val = divmod(ans, 10)
            old_head = head
            head = ListNode(val)
            head.next = old_head
        return head

    def addTwoNumbers(self, l1, l2):
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        sentry = ListNode(0)
        cur = sentry
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            val, carry = s % 10, s//10
            cur.next = ListNode(val)
            cur = cur.next
        return self.reverse(sentry.next)

    def reverse(self, l):
        pre = None
        while l:
            l.next, l, pre = pre, l.next, l
        return pre

# @lc code=end
