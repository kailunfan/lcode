#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode-cn.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (76.93%)
# Likes:    462
# Dislikes: 0
# Total Accepted:    70.4K
# Total Submissions: 91.2K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL
# 的节点将直接作为新二叉树的节点。
#
# 示例 1:
#
#
# 输入:
# Tree 1                     Tree 2
# ⁠         1                         2
# ⁠        / \                       / \
# ⁠       3   2                     1   3
# ⁠      /                           \   \
# ⁠     5                             4   7
# 输出:
# 合并后的树:
# 3
# / \
# 4   5
# / \   \
# 5   4   7
#
#
# 注意: 合并必须从两个树的根节点开始。
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 迭代
        if not t1 or not t2:
            return t1 or t2
        stack = [(t1, t2)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 or not n2:
                continue
            n1.val += n2.val
            if not n1.left:
                n1.left = n2.left
            else:
                stack.append((n1.left, n2.left))
            if not n1.right:
                n1.right = n2.right
            else:
                stack.append((n1.right, n2.right))
        return t1

        # 递归
        if not t1 or not t2:
            return t1 or t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

        # 迭代,不修改原来的树
        if not t1 and not t2:
            return None

        ans = TreeNode(0)
        stack = [(t1, t2, ans)]
        while stack:
            n1, n2, n3 = stack.pop()
            if n1 or n2:
                n3.val += n1.val if n1 else 0
                n3.val += n2.val if n2 else 0
                if n1 and n1.left or n2 and n2.left:
                    n3.left = TreeNode(0)
                if n1 and n1.right or n2 and n2.right:
                    n3.right = TreeNode(0)
                stack.append((n1.right if n1 else None, n2.right if n2 else None, n3.right))
                stack.append((n1.left if n1 else None, n2.left if n2 else None, n3.left))
        return ans


# @lc code=end
