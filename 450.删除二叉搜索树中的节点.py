#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#
# https://leetcode-cn.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (39.77%)
# Likes:    199
# Dislikes: 0
# Total Accepted:    13.6K
# Total Submissions: 33.4K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key
# 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。
#
#
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。
#
# 示例:
#
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
#
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
#
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
#
# 另一个正确答案是 [5,2,6,null,4,null,7]。
#
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
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
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # 迭代
        # if not root:
        #     return
        # sentry = TreeNode(None)
        # sentry.left = root
        # # (node,node.parent,left|right)
        # stack = [(root, sentry, 'left')]
        # while stack:
        #     node, par, direction = stack.pop()
        #     if node.val > key and node.left:
        #         stack.append((node.left, node, 'left'))
        #     elif node.val < key and node.right:
        #         stack.append((node.right, node, 'right'))
        #     elif node.val == key:
        #         # 删除节点
        #         target = None
        #         if node.left and node.right:
        #             # 找到左子树中的最大值
        #             cur = node.left
        #             while cur.right:
        #                 cur = cur.right
        #             cur.right = node.right
        #             target = node.left
        #         else:
        #             target = node.left or node.right
        #         setattr(par, direction, target)
        # return sentry.left

        # 递归
        def search(node):
            if not node:
                return node
            if node.val > key:
                node.left = search(node.left)
                return node
            if node.val < key:
                node.right = search(node.right)
                return node
            # 相等的情况
            if node.left and node.right:
                # 找到左子树中的最大值
                cur = node.left
                while cur.right:
                    cur = cur.right
                cur.right = node.right
                return node.left
            return node.left or node.right
            
        return search(root)

        def delete(node, key):
            if not node:
                return None
            if key > node.val:
                node.right = delete(node.right, key)
                return node
            if key < node.val:
                node.left = delete(node.left, key)
                return node
            # node就是要删除的节点
            if not node.left and not node.right:
                node = None
            elif node.right:
                # 找右子树中最小的值
                cur = node.right
                while cur.left:
                    cur = cur.left
                node.val = cur.val
                node.right = delete(node.right, cur.val)
            else:
                # 找左子树中最大的值
                cur = node.left
                while cur.right:
                    cur = cur.right
                node.val = cur.val
                node.left = delete(node.left, cur.val)
            return node
        return delete(root, key)


# @lc code=end
