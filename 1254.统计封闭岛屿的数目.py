#
# @lc app=leetcode.cn id=1254 lang=python
#
# [1254] 统计封闭岛屿的数目
#
# https://leetcode-cn.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (58.71%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 9.2K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# 有一个二维矩阵 grid ，每个位置要么是陆地（记号为 0 ）要么是水域（记号为 1 ）。
# 
# 我们从一块陆地出发，每次可以往上下左右 4 个方向相邻区域走，能走到的所有陆地区域，我们将其称为一座「岛屿」。
# 
# 如果一座岛屿 完全 由水域包围，即陆地边缘上下左右所有相邻区域都是水域，那么我们将其称为 「封闭岛屿」。
# 
# 请返回封闭岛屿的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# 输出：2
# 解释：
# 灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
# 
# 示例 2：
# 
# 
# 
# 输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠            [1,1,1,1,1,1,1]]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
# 
# 
#

# @lc code=start
class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])

        def neighbors(r,c):
            for nr,nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
                if 0<=nr<R and 0<=nc<C:
                    yield nr,nc
        
        ans = 0
        seen = set()
        for r,row in enumerate(grid):
            for c,val in enumerate(row):
                if val == 0 and (r,c) not in seen:
                    this_island = {(r,c)}
                    stack = [(r,c)]
                    at_adge = False
                    while stack:
                        node = stack.pop()
                        if node[0] in [0,R-1] or node[1] in [0, C-1]:
                            at_adge = True
                        for nei in neighbors(*node):
                            if grid[nei[0]][nei[1]]==0 and nei not in this_island:
                                stack.append(nei)
                                this_island.add(nei)
                    if not at_adge:
                        ans += 1
                    seen.update(this_island)
        return ans


            
# @lc code=end

