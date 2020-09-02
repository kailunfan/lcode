#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (50.78%)
# Likes:    762
# Dislikes: 0
# Total Accepted:    136.3K
# Total Submissions: 267K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
#
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠    1
# ⁠  /   \
# ⁠ 2     2
# ⁠/ \   / \
# 3  4  4  3
#
#
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# 进阶：
#
# 你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 递归
        def check(ln, rn):
            if not ln and not rn:
                return True
            if not ln or not rn:
                return False
            if ln.val != rn.val:
                return False
            return check(ln.left, rn.right) and check(ln.right, rn.left)
        if not root:
            return True
        return check(root.left,root.right)

        # 深度遍历(最优)
        # 前左右和前右左比较
        stack = [(root, root)]
        while stack:
            ln, rn = stack.pop()
            if not any([ln, rn]):
                continue
            if not all([ln, rn]):
                return False
            if ln.val != rn.val:
                return False
            stack.append((ln.left, rn.right))
            stack.append((ln.right, rn.left))
        return True

        # 广度遍历,判断每层
        layer = [root]
        while layer:
            values = []
            this_layer = []
            for node in layer:
                values.append(node and node.val)
                if node:
                    this_layer.extend([node.left, node.right])
            # check
            lc, rc = 0, len(values)-1
            while lc < rc:
                if values[lc] != values[rc]:
                    return False
                lc += 1
                rc -= 1
            # change
            layer = this_layer
        return True

# @lc code=end
