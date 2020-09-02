#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (42.07%)
# Likes:    257
# Dislikes: 0
# Total Accepted:    75.9K
# Total Submissions: 178.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        # 深度优先(前序)(没有剪枝,复杂度较高)
        ans = float('inf')
        stack = [(root,1)]
        while stack:
            node,depth = stack.pop()
            if not node.left and not node.right and depth < ans:
                ans = depth
            if node.right:
                stack.append((node.right,depth+1))
            if node.left:
                stack.append((node.left,depth+1))
        return ans

        
        # 层次遍历
        stack = [root]
        depth = 0
        while stack:
            depth += 1
            tmp_stack = []
            for i in stack:
                if i:
                    if not i.left and not i.right:
                        return depth
                    tmp_stack.append(i.left)
                    tmp_stack.append(i.right)
            stack = tmp_stack
        return depth
# @lc code=end

