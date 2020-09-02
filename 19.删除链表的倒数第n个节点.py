#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (38.34%)
# Likes:    871
# Dislikes: 0
# Total Accepted:    189.6K
# Total Submissions: 487.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 
# 示例：
# 
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
# 
# 说明：
# 
# 给定的 n 保证是有效的。
# 
# 进阶：
# 
# 你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # lc = rc = head
        # for i in range(n):
        #     rc = rc.next
        #     if not rc: # 关键点
        #         return head.next

        # while rc.next:
        #     rc = rc.next
        #     lc = lc.next
        # lc.next = lc.next.next
        # return head

        # 引入哨兵
        sentry = ListNode(None)
        sentry.next = head
        lc = rc = sentry
        # 先走
        for i in range(n):
            rc = rc.next
        
        # 一起走,注意结束条件
        while rc.next:
            lc = lc.next
            rc = rc.next
        lc.next = lc.next.next
        return sentry.next
# @lc code=end

