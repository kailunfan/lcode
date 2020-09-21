#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.98%)
# Likes:    666
# Dislikes: 0
# Total Accepted:    121.7K
# Total Submissions: 236K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 标准解法
        # 维护k个指针
        sentry = ListNode(None)
        cur = sentry
        heads = []
        for head in lists:
            if head:
                heads.append((head.val, head))
        heapq.heapify(heads)
        while heads:
            _, node = heapq.heappop(heads)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heads,(node.next.val,node.next))
        return sentry.next

        # 分治(归并)
        if not lists:
            return None
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                if i+1 < len(lists):
                    tmp.append(self.merger_two(lists[i], lists[i+1]))
                else:
                    tmp.append(lists[i])
            lists = tmp
        return lists[0]

    @staticmethod
    def merger_two(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        sentry = ListNode(None)
        cur = sentry
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return sentry.next


# @lc code=end
