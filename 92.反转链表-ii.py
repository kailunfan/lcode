#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (49.68%)
# Likes:    384
# Dislikes: 0
# Total Accepted:    53.7K
# Total Submissions: 107K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        sentry = ListNode(0)
        sentry.next = head
        pre_tail = sentry
        for _ in range(m-1):
            pre_tail = pre_tail.next

        this_head = pre_tail.next
        cur = this_head
        pre = None
        for _ in range(n-m+1):
            cur.next, cur, pre = pre, cur.next, cur
        pre_tail.next = pre
        this_head.next = cur
        return sentry.next

        # @lc code=end
