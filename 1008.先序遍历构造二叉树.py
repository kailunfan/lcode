#
# @lc app=leetcode.cn id=1008 lang=python
#
# [1008] 先序遍历构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (71.91%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 8.8K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# 返回与给定先序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
# 
# (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right
# 的任何后代，值总 > node.val。此外，先序遍历首先显示节点的值，然后遍历 node.left，接着遍历 node.right。）
# 
# 
# 
# 示例：
# 
# 输入：[8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= preorder.length <= 100
# 先序 preorder 中的值是不同的。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def build(list):
            if not list:
                return None
            base = list[0]
            node = TreeNode(base)
            node.left = build([i for i in list if i < base])
            node.right = build([i for i in list if i > base])
            return node
        return build(preorder)
# @lc code=end

