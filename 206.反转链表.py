#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (68.56%)
# Likes:    997
# Dislikes: 0
# Total Accepted:    253.1K
# Total Submissions: 365.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 注意,解构赋值的原理
        # a,b,c = d,e,f
        # 相当于 x = (d,e,f)
        # 再执行 a = d, b = e, c = f
        # 所以解构赋值左值中,后面的变量一定不能用到前面的变量.
        pre, cur = None, head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre

        # 递归
        def rev(node):
            # return new_head,tail
            if not node or not node.next:
                return node, node
            tmp = node.next
            node.next = None
            new_head, tail = rev(tmp)
            tail.next = node
            return new_head, node

        new_head, _ = rev(head)
        return new_head


# @lc code=end
