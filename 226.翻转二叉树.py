#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#
# https://leetcode-cn.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (74.79%)
# Likes:    443
# Dislikes: 0
# Total Accepted:    80.1K
# Total Submissions: 106.5K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
#
# 输出：
#
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
#
# 备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
# 谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 递归
        # def build(node):
        #     if not node:
        #         return None
        #     node.left, node.right = build(node.right), build(node.left)
        #     return node
        # build(root)
        # return root
        # 迭代
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left,node.right = node.right,node.left
        return root
            



# @lc code=end
