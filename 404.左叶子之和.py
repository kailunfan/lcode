#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (54.26%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    25K
# Total Submissions: 45.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root or (not root.left and not root.right):
            return 0
        layer = [root]
        ans = 0
        while layer:
            tmp = []
            for node in layer:
                if node.left and not node.left.left and not node.left.right:
                    ans += node.left.val
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            layer = tmp
        return ans

# @lc code=endP
