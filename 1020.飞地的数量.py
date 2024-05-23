#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
# https://leetcode.cn/problems/number-of-enclaves/description/
#
# algorithms
# Medium (61.77%)
# Likes:    265
# Dislikes: 0
# Total Accepted:    77.3K
# Total Submissions: 125.4K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
#
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
#
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#
#
# 示例 2：
#
#
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1
#
#
#

# @lc code=start
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        state = [[False]*n for _ in range(m)]

        def visit(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or state[r][c]:
                return
            state[r][c] = True
            for i in ([r-1, c], [r+1, c], [r, c+1], [r, c-1]):
                visit(i[0], i[1])

        for i in range(m):
            visit(i, 0)
            visit(i, n-1)
        for j in range(1, n-1):
            visit(0, j)
            visit(m-1, j)

        ans = 0
        for i in range(m):
            for j in range(n):
                if not state[i][j] and grid[i][j] == 1:
                    ans += 1
        return ans

# @lc code=end
