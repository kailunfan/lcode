#
# @lc app=leetcode.cn id=109 lang=python
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (71.59%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    29.4K
# Total Submissions: 40.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
#
#
#

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# @lc code=start
# Definition for singly-linked list.


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        def build(head, tail):
            if head == tail:
                return
            mid = self.mid(head, tail)
            node = TreeNode(mid.val)
            node.left = build(head, mid)
            node.right = build(mid.next, tail)
            return node
        return build(head, None)

    def mid(self, l, r):
        lc, rc = l, l
        while rc != r and rc.next != r:
            lc = lc.next
            rc = rc.next.next
        return lc

# @lc code=end
