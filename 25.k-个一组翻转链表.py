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

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        # 迭代
        # 头
        if not head:
            return head
        ans = head
        for i in range(k-1):
            ans = ans.next
            if not ans:
                return head
        while head:
            pre,cur = None,head
            for i in range(k):
                cur.next,cur,pre = pre,cur.next,cur
            # 检查剩余元素
            c = cur
            if not c:
                return ans
            for i in range(k-1):
                c = c.next
                if not c:
                    head.next = cur
                    return ans
            head.next = c
            head = cur
        return ans
                
        # 递归
        if not head:
            return head
        cur = head
        for i in range(k-1):
            cur = cur.next
            if not cur:
                return head
        pre, cur = self.reverseKGroup(cur.next, k), head
        for i in range(k):
            cur.next, cur, pre = pre, cur.next, cur
        return pre

# @lc code=end
