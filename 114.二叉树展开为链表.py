#
# @lc app=leetcode.cn id=114 lang=python
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (68.43%)
# Likes:    348
# Dislikes: 0
# Total Accepted:    41.8K
# Total Submissions: 60.6K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为一个单链表。
#
#
#
# 例如，给定二叉树
#
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
#
# 将其展开为：
#
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 迭代
        # 1. 前序遍历,最后的节点在root.right.right.right...
        # 2. 要将左子树插到右子树前
        #   - 找到左子树最后节点
        #   - 将右子树插进去
        #   - 调整根节点
        cur = root
        while cur:
            if cur.left:
                lend = cur.left
                while lend.right:
                    lend = lend.right
                lend.right = cur.right
                cur.right, cur.left = cur.left, None
            cur = cur.right

        return

        # 递归
        def build(node):
            if not node:
                return node
            lc = build(node.left)
            rc = build(node.right)
            node.left = None
            if not lc:
                node.right = rc
                return node

            node.right = lc
            cur = lc
            while cur.right:
                cur = cur.right
            cur.right = rc
            return node

        build(root)
# @lc code=end
