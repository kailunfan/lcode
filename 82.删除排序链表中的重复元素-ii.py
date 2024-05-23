#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (47.28%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    48.7K
# Total Submissions: 101.6K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        sentry = ListNode(None)
        sentry.next = head
        cur = sentry
        while cur and cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                v = cur.next.val
                rc = cur.next.next.next
                while rc and rc.val == v:
                    rc = rc.next
                cur.next = rc
            else:
                cur = cur.next
        return sentry.next


# @lc code=end
