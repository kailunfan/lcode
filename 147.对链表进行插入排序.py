#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (63.88%)
# Likes:    200
# Dislikes: 0
# Total Accepted:    37.1K
# Total Submissions: 57.1K
# Testcase Example:  '[4,2,1,3]'
#
# 对链表进行插入排序。
#
#
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
#
#
# 插入排序算法：
#
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
#
#
#
# 示例 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2：
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#
#
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(float('-inf'))
        dummy.next = head

        cur = head
        while cur and cur.next:
            if cur.next.val > cur.val:
                cur = cur.next
            else:
                lc = dummy
                while lc.next.val < cur.next.val:
                    lc = lc.next
                lc.next,  cur.next.next, cur.next = cur.next, lc.next, cur.next.next
        return dummy.next

# @lc code=end
