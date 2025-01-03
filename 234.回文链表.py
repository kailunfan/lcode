#
# @lc app=leetcode.cn id=234 lang=python
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (41.44%)
# Likes:    521
# Dislikes: 0
# Total Accepted:    94.5K
# Total Submissions: 224.5K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        stack = []
        lc = rc = head
        while rc and rc.next:
            stack.append(lc.val)
            lc = lc.next
            rc = rc.next.next
        if rc:
            lc = lc.next
        while stack:
            if lc.val != stack.pop():
                return False
            lc = lc.next
        return True

    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        s.next, newHead = None, s.next

        pre = None
        cur = newHead
        while cur:
            cur.next, cur, pre = pre, cur.next, cur

        newHead = pre

        l1, l2 = head, newHead
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True


# @lc code=end
