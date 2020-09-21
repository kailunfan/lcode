#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#
# https://leetcode-cn.com/problems/maximum-binary-tree/description/
#
# algorithms
# Medium (81.30%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 24.1K
# Testcase Example:  '[3,2,1,6,0,5]'
#
# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
#
#
# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。
#
#
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。
#
#
#
# 示例 ：
#
# 输入：[3,2,1,6,0,5]
# 输出：返回下面这棵树的根节点：
#
# ⁠     6
# ⁠   /   \
# ⁠  3     5
# ⁠   \    /
# ⁠    2  0
# ⁠      \
# ⁠       1
#
#
#
#
# 提示：
#
#
# 给定的数组的大小在 [1, 1000] 之间。
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def build(li):
            if not li:
                return
            m = max(li)
            ind = li.index(m)
            node = TreeNode(m)
            node.left = build(li[:ind])
            node.right = build(li[ind+1:])
            return node
        return build(nums)

# @lc code=end
