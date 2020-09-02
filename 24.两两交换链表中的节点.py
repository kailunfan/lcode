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

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 这道题用递归so easy啊.
        if not head or not head.next:
            return head
        next = head.next
        tmp = next.next
        next.next = head
        head.next = self.swapPairs(tmp)
        return next

        # 迭代试试吧
        # if not head or not head.next:
        #     return head
        # ans = head.next
        # c1 = head
        # c2 = head.next
        # while c2:
        #     tar = None
        #     next_c1 = None
        #     if c2.next:
        #         next_c1 = c2.next
        #         if c2.next.next:
        #             tar = c2.next.next
        #         else:
        #             tar = c2.next
        #     c2.next = c1
        #     c1.next = tar
        #     c1 = next_c1
        #     c2 = c1 and c1.next
        # return ans
            


        
# @lc code=end

