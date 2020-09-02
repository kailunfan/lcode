#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (55.64%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    33.1K
# Total Submissions: 58.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 示例 1:
# 
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 
# 示例 2:
# 
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找出中点
        # 反转后半部分
        # 合并
        if not head:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # 反转
        pre = None
        cur = mid
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        # 合并
        lhead = head
        rhead = pre
        new_head = lhead
        target = rhead
        while target:
            tmp = new_head.next
            new_head.next = target
            new_head = target
            target = tmp
        return new_head


        
# @lc code=end

