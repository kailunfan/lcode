#
# @lc app=leetcode.cn id=129 lang=python
#
# [129] 求根到叶子节点数字之和
#
# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (62.76%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    27.1K
# Total Submissions: 42.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
#
# 例如，从根到叶子节点路径 1->2->3 代表数字 123。
#
# 计算从根到叶子节点生成的所有数字之和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例 1:
#
# 输入: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# 输出: 25
# 解释:
# 从根到叶子节点路径 1->2 代表数字 12.
# 从根到叶子节点路径 1->3 代表数字 13.
# 因此，数字总和 = 12 + 13 = 25.
#
# 示例 2:
#
# 输入: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# 输出: 1026
# 解释:
# 从根到叶子节点路径 4->9->5 代表数字 495.
# 从根到叶子节点路径 4->9->1 代表数字 491.
# 从根到叶子节点路径 4->0 代表数字 40.
# 因此，数字总和 = 495 + 491 + 40 = 1026.
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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # 组合栈
        ans = 0
        stack = [(root, root.val)]
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right:
                ans += s
            if node.left:
                stack.append((node.left, 10*s+node.left.val))
            if node.right:
                stack.append((node.right, 10*s+node.right.val))
        return ans

        # 层次遍历
        # root.sum = root.val
        # stack = [root]
        # res = 0
        # while stack:
        #     new_stack = []
        #     for i in stack:
        #         if not i.left and not i.right:
        #             res += i.sum
        #         else:
        #             if i.left:
        #                 i.left.sum = i.sum * 10 + i.left.val
        #                 new_stack.append(i.left)
        #             if i.right:
        #                 i.right.sum = i.sum * 10 + i.right.val
        #                 new_stack.append(i.right)
        #     stack = new_stack
        # return res


# @lc code=end
