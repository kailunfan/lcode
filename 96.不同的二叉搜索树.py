#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (65.19%)
# Likes:    511
# Dislikes: 0
# Total Accepted:    43.4K
# Total Submissions: 66.2K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#

# @lc code=start

from functools import lru_cache

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        @lru_cache(None)
        def search(n):
            if n <= 1:
                return 1
            ans = 0
            for i in range(n):
                ans += search(i) * search(n-i-1)
            return ans
        return search(n)

# @lc code=end
