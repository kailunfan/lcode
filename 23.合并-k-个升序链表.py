#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (57.68%)
# Likes:    2401
# Dislikes: 0
# Total Accepted:    627.5K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
# 示例 2：
#
# 输入：lists = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
#
#
# 提示：
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
#
#
#

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.


class Solution:
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sentry = ListNode()
        cur = sentry
        while True:
            min_node = None
            min_ind = 0
            for i, n in enumerate(lists):
                if not n:
                    continue
                if not min_node or n.val < min_node.val:
                    min_node = n
                    min_ind = i
            if not min_node:
                break
            cur.next = min_node
            cur = cur.next
            lists[min_ind] = min_node.next
        return sentry.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 两两合并
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            this_lists = []
            l, r = 0, len(lists)-1
            while l < r:
                this_lists.append(self.merge_two(lists[l], lists[r]))
                l += 1
                r -= 1
            if l == r:
                this_lists.append(lists[l])
            lists = this_lists
        return lists[0]

    def merge_two(self, list1, list2):
        sentry = ListNode()
        cur = sentry
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return sentry.next

# @lc code=end
