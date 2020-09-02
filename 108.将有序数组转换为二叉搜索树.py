#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (70.37%)
# Likes:    413
# Dislikes: 0
# Total Accepted:    67.9K
# Total Submissions: 95.8K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        def build(start, end):
            if start > end:
                return
            mi = (start + end + 1) // 2
            root = TreeNode(nums[mi])
            root.left = build(start, mi-1)
            root.right = build(mi+1, end)
            return root
        return build(0, len(nums)-1)

        # 额外空间占用
        mi = len(nums) // 2
        mv = nums[mi]
        root = TreeNode(mv)
        root.left = self.sortedArrayToBST(nums[0:mi])
        root.right = self.sortedArrayToBST(nums[mi+1:])
        return root

# @lc code=end
