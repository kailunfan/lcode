#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (54.19%)
# Likes:    189
# Dislikes: 0
# Total Accepted:    48.5K
# Total Submissions: 89.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        reverse = False
        stack = [root]
        res = []
        while stack:
            tmp_res = []
            tmp_stack = []
            for i in stack:
                if i:
                    tmp_res.append(i.val)
                    tmp_stack.append(i.left)
                    tmp_stack.append(i.right)
            if tmp_res:
                if reverse:
                    res.append(tmp_res[::-1])
                else:
                    res.append(tmp_res)
            reverse = not reverse
            stack = tmp_stack
        return res

        
# @lc code=end

