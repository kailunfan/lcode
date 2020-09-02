#
# @lc app=leetcode.cn id=543 lang=python
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (49.52%)
# Likes:    352
# Dislikes: 0
# Total Accepted:    49.6K
# Total Submissions: 99.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
# 示例 :
# 给定二叉树
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
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
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.ans = 0
        def search(node):
            if not node:
                return 0
            l = search(node.left)
            r = search(node.right)
            self.ans = max(self.ans, l + r + 1)
            return max(l, r) + 1
        
        search(root)
        return self.ans - 1

# @lc code=end
