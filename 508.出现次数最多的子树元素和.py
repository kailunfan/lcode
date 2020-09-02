#
# @lc app=leetcode.cn id=508 lang=python
#
# [508] 出现次数最多的子树元素和
#
# https://leetcode-cn.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (63.05%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    5.9K
# Total Submissions: 9.1K
# Testcase Example:  '[5,2,-3]'
#
# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
#
# 你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
#
#
#
# 示例 1：
# 输入:
#
# ⁠ 5
# ⁠/  \
# 2   -3
#
#
# 返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
#
# 示例 2：
# 输入：
#
# ⁠ 5
# ⁠/  \
# 2   -5
#
#
# 返回 [2]，只有 2 出现两次，-5 只出现 1 次。
#
#
#
# 提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.res = []

        def search(node):
            if not node:
                return 0
            res = node.val + search(node.left) + search(node.right)
            self.res.append(res)
            return res
        search(root)
        res = Counter(self.res).most_common()
        ans = []
        base = res[0][1]
        for i in res:
            if i[1] == res[0][1]:
                ans.append(i[0])
        return ans

# @lc code=end
