#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (64.31%)
# Likes:    426
# Dislikes: 0
# Total Accepted:    63.2K
# Total Submissions: 97.3K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
#
#
#
# 例如，给定三角形：
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#
#

# @lc code=start


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 回溯
        for r, row in enumerate(triangle):
            if r == 0:
                continue
            for c, val in enumerate(row):
                left_increase = right_increase = float('inf')
                if c > 0:
                    left_increase = triangle[r-1][c-1]
                if c < len(row) - 1:
                    right_increase = triangle[r-1][c]
                triangle[r][c] += min(left_increase,right_increase)

        return min(triangle[-1])



# @lc code=end
