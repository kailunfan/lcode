#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (54.76%)
# Likes:    413
# Dislikes: 0
# Total Accepted:    34.4K
# Total Submissions: 62.5K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        ans = 0
        # 回溯
        def search(node, res_list):
            nonlocal ans
            ans += res_list.count(sum)
            if node.left:
                search(node.left, [i+node.left.val for i in res_list]+[node.left.val])
            if node.right:
                search(node.right, [i+node.right.val for i in res_list]+[node.right.val])
        search(root, [root.val])
        return ans


# @lc code=end
