#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (72.82%)
# Likes:    535
# Dislikes: 0
# Total Accepted:    175.8K
# Total Submissions: 240.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        layer = [root]
        depth = 0
        while layer:
            depth += 1
            tmp = []
            for i in layer:
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            layer = tmp
            
        return depth
            
# @lc code=end

