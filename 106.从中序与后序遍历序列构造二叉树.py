#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (67.87%)
# Likes:    204
# Dislikes: 0
# Total Accepted:    36.3K
# Total Submissions: 52.9K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 根据一棵树的中序遍历与后序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        l = len(postorder)
        order_map = {item: (l-ind) for ind,item in enumerate(postorder)}

        def build(li):
            if not li:
                return None
            if len(li) == 1:
                return TreeNode(li[0])
            min_val = li[0]
            min_index = 0
            for (ind,item) in enumerate(li):
                if order_map[item] < order_map[min_val]:
                    min_val = item
                    min_index = ind
            root = TreeNode(min_val)
            root.left = build(li[:min_index])
            root.right = build(li[min_index+1:])
            return root
        return build(inorder)

# @lc code=end

