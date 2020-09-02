#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (57.09%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 70.6K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
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
    def partition(self, head: ListNode, x: int) -> ListNode:
        lhead, rhead = ListNode(None), ListNode(None)
        lc, rc = lhead, rhead
        cur = head
        while cur:
            if cur.val < x:
                lc.next = cur
                lc = cur
            else:
                rc.next = cur
                rc = cur
            cur = cur.next
        lc.next = rhead.next
        # 关键点
        rc.next = None
        return lhead.next
# @lc code=end
