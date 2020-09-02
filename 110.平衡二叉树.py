#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (51.30%)
# Likes:    318
# Dislikes: 0
# Total Accepted:    75.5K
# Total Submissions: 145.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
# 本题中，一棵高度平衡二叉树定义为：
#
#
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
#
#
# 示例 1:
#
# 给定二叉树 [3,9,20,null,null,15,7]
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回 true 。
#
# 示例 2:
#
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# 返回 false 。
#
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    isb = True
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.height(root)
        return self.isb

    def height(self,node):
        if not node:
            return 0
        # 剪枝
        if not self.isb:
            return 0
        lh = self.height(node.left)
        rh = self.height(node.right)
        if abs(lh - rh) > 1:
            self.isb = False
        return max(lh, rh) + 1
# @lc code=end
