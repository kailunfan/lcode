#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (65.20%)
# Likes:    535
# Dislikes: 0
# Total Accepted:    118K
# Total Submissions: 178.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 这道题用递归so easy啊.
        # if not head or not head.next:
        #     return head
        # head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        # return head

        # 迭代
        sentry = ListNode(0)
        sentry.next = head
        cur = sentry
        while cur and cur.next and cur.next.next:
            cur.next.next.next, cur.next.next,      cur.next,      cur = \
            cur.next,           cur.next.next.next, cur.next.next, cur.next
        return sentry.next
    # @lc code=end
