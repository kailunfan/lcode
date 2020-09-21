#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (60.34%)
# Likes:    253
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 42.6K
# Testcase Example:  '[5,2,13]'
#
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater
# Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
#
#
# 例如：
#
# 输入: 原始二叉搜索树:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
#
# 输出: 转换为累加树:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
#
#
#
#
# 注意：本题和 1038:
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
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
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 右中左遍历,累加
        stack = []
        cur = root
        p_val = 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                # 逻辑
                cur.val += p_val
                p_val = cur.val
                cur = cur.left
        return root


# @lc code=end
