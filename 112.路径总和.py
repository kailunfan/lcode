#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (49.50%)
# Likes:    303
# Dislikes: 0
# Total Accepted:    76.7K
# Total Submissions: 154.5K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
# 
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
# 
# 
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
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
    res = False
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            if sum == root.val:
                return True
            return False

        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


# @lc code=end

