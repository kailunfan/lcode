#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (58.07%)
# Likes:    614
# Dislikes: 0
# Total Accepted:    77.2K
# Total Submissions: 125.5K
# Testcase Example:  '[1,2,3]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
#
# 示例：
#
# 给你这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
#
#
# 说明：
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        sentry = ListNode(None)
        pre_tail = sentry
        next_head = head

        while True:
            this_head = next_head
            for _ in range(k):
                if not next_head:
                    pre_tail.next = this_head
                    return sentry.next
                next_head = next_head.next

            pre = next_head
            cur = this_head
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur
            pre_tail.next = pre
            pre_tail = this_head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        cur = head
        for _ in range(k-1):
            cur = cur.next
            if not cur:
                return head

        next_head = self.reverseKGroup(cur.next, k)
        pre = next_head
        cur = head
        for _ in range(k):
            cur.next, cur, pre = pre, cur.next, cur
        return pre

    # @lc code=end
