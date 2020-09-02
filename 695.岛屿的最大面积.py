#
# @lc app=leetcode.cn id=695 lang=python
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (63.31%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    49.5K
# Total Submissions: 77.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。
# 
# 一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被
# 0（代表水）包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)
# 
# 
# 
# 示例 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。
# 
# 示例 2:
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R = len(grid)
        C = len(grid[0])

        def neighbors(r,c):
            for nr,nc in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
                if 0<=nr<R and 0<=nc<C:
                    yield nr,nc

        # 深先搜索
        seen = set()
        islands = []
        ans = 0

        for r,row in enumerate(grid):
            for c,val in enumerate(row):
                if not val or (r,c) in seen:
                    continue
                this_island = {(r,c)}
                stack = [(r,c)]
                while stack:
                    node = stack.pop()
                    for nei in neighbors(*node):
                        if grid[nei[0]][nei[1]] and nei not in this_island:
                            this_island.add(nei)
                            stack.append(nei)
                seen |= this_island
                ans = max(ans,len(this_island))
        return ans
                        

        

        
# @lc code=end

