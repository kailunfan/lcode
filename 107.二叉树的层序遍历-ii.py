#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Medium (73.77%)
# Likes:    790
# Dislikes: 0
# Total Accepted:    330.8K
# Total Submissions: 447.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[15,7],[9,20],[3]]
#
#
# 示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
# 示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        layer = [root]
        res = []
        while layer:
            this_layer = []
            this_res = []
            for i in layer:
                this_res.append(i.val)
                if i.left:
                    this_layer.append(i.left)
                if i.right:
                    this_layer.append(i.right)
            layer = this_layer
            res.append(this_res)
        res.reverse()
        return res
    

# @lc code=end
