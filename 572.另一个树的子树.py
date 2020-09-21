#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#
# https://leetcode-cn.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (46.95%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    48.8K
# Total Submissions: 103.7K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s
# 也可以看做它自身的一棵子树。
#
# 示例 1:
# 给定的树 s:
#
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
#
#
# 给定的树 t：
#
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
#
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
#
# 示例 2:
# 给定的树 s：
#
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
#
#
# 给定的树 t：
#
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
#
# 返回 false。
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
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def search(node):
            if not node:
                return False
            if self.same(node, t):
                return True
            return search(node.left) or search(node.right)
        return search(s)

    def same(self,node1, node2):
        stack = [(node1, node2)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                stack.append((n1.left, n2.left))
                stack.append((n1.right, n2.right))
            elif n1 or n2:
                return False
        return True


# @lc code=end
