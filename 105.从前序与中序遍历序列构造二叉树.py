#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (64.96%)
# Likes:    484
# Dislikes: 0
# Total Accepted:    76.9K
# Total Submissions: 115.3K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
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

# @lc code=start
# Definition for a binary tree node.


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    ind = 0
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        order_map = {item: ind for ind,item in enumerate(preorder)}

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
