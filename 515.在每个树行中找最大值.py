#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#
# https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (59.31%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 19.2K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 您需要在二叉树的每一行中找到最大的值。
# 
# 示例：
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \  
# ⁠     5   3   9 
# 
# 输出: [1, 3, 9]
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            this_max = float('-inf')
            tmp_stack = []
            for i in stack:
                if i.val > this_max:
                    this_max = i.val
                if i.left:
                    tmp_stack.append(i.left)
                if i.right:
                    tmp_stack.append(i.right)
            res.append(this_max)
            stack = tmp_stack
        return res
        
# @lc code=end

