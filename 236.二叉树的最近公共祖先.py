#
# @lc app=leetcode.cn id=236 lang=python
#
# [236] 二叉树的最近公共祖先
#
# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (61.45%)
# Likes:    573
# Dislikes: 0
# Total Accepted:    84.2K
# Total Submissions: 132.1K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x
# 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#
#
# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
#
# 示例 2:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#
#
#
#
# 说明:
#
#
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # def search(node):
        #     """
        #     1. 返回值是啥
        #         - 返回的是一个节点;
        #          - 这个节点或者是p或者q本身,或者是他们的最近公共祖先;
        #          - 将这个节点一直向上传递;
        #     2. 有啥副作用
        #     ====== 以上这些可以不关注么?
        #     1. 返回的就是局部结果;
        #     2. 递归调用,自己没有结果,则去儿子找;
        #     """
        #     if not node:
        #         return None
        #     # 重点
        #     if node == p or node == q:
        #         return node
        #     left = search(node.left)
        #     right = search(node.right)
        #     # 一种特殊情况
        #     if left and right:
        #         return node
        #     # 重点,将结果向上传递
        #     return left or right
        # return search(root)

        def search(node):
            if not node:
                return
            if node in [p,q]:
                return node
            lans = search(node.left)
            rans = search(node.right)
            if lans and rans:
                return node
            return lans or rans

        return search(root)


# @lc code=end
