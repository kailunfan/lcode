#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (62.42%)
# Likes:    390
# Dislikes: 0
# Total Accepted:    30.4K
# Total Submissions: 48.6K
# Testcase Example:  '3'
#
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
#
# 示例:
#
# 输入: 3
# 输出:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n<=0:
            return []
        # 回溯
        def build(start,end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            ans = []
            for i in range(start,end+1):
                for x in build(start,i-1):
                    for y in build(i+1,end):
                        tree = TreeNode(i)
                        tree.left = x
                        tree.right = y
                        ans.append(tree)
            return ans

        return build(1,n)

# @lc code=end
