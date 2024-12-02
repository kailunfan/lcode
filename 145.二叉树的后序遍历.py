#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (71.08%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    78.3K
# Total Submissions: 109.6K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]  
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3 
# 
# 输出: [3,2,1]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归
        res = []
        def tranverse(node):
            if not node:
                return
            tranverse(node.left)
            tranverse(node.right)
            res.append(node.val)
        tranverse(root)
        return res
            

        
        # 前序遍历的变种
        stack,res = [],[]
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left
        return res[::-1]


# @lc code=end

