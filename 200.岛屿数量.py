#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (48.08%)
# Likes:    614
# Dislikes: 0
# Total Accepted:    118.4K
# Total Submissions: 238.8K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#
#

# @lc code=start


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        ans = 0
        R = len(grid)
        C = len(grid[0])

        def neighbors(r, c):
            for nr, nc in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        seen = set()

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val =='0' or (r, c) in seen:
                    continue
                ans += 1
                this_island = {(r, c)}
                stack = [(r, c)]
                while stack:
                    node = stack.pop()
                    for nei in neighbors(*node):
                        if grid[nei[0]][nei[1]] == '1' and nei not in this_island:
                            this_island.add(nei)
                            stack.append(nei)
                seen |= this_island

        return ans


# @lc code=end
