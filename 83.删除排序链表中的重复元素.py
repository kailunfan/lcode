#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (49.99%)
# Likes:    319
# Dislikes: 0
# Total Accepted:    106.3K
# Total Submissions: 210.6K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 
# 示例 1:
# 
# 输入: 1->1->2
# 输出: 1->2
# 
# 
# 示例 2:
# 
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
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
        cur = head
        while cur and cur.next:
            rc = cur.next
            while rc and rc.val == cur.val:
                rc = rc.next
            # 优化
            if cur.next != rc:
                cur.next = rc
            cur = rc
        return head


        # while cur and cur.next:
        #     lc = cur.next
        #     if lc.val != cur.val:
        #         cur = lc
        #         continue
        #     while rc and rc.val == cur.val:
        #         rc = rc.next
        #     cur.next = rc
        #     cur = rc
        # return head




# @lc code=end

