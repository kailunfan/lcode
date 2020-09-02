#
# @lc app=leetcode.cn id=404 lang=python
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
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        stack = [root]
        ans = 0
        while stack:
            tmp_stack = []
            for i in stack:
                if i.left and not i.left.left and not i.left.right:
                    ans += i.left.val
                if i.left:
                    tmp_stack.append(i.left)
                if i.right:
                    tmp_stack.append(i.right)
            stack = tmp_stack
        return ans
        
# @lc code=endP

