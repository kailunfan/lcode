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

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start
# Definition for a binary tree node.


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(prelist, inlist):
            if len(prelist) == 0:
                return None
            val = prelist[0]
            # idx = inorder_ind_map[val]
            idx = inlist.index(val)
            root = TreeNode(val)
            root.left = build(prelist[1:idx+1], inlist[:idx])
            root.right = build(prelist[idx+1:], inlist[idx+1:])
            return root

        return build(preorder, inorder)

# @lc code=end
