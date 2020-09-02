#
# @lc app=leetcode.cn id=463 lang=python
#
# [463] 岛屿的周长
#
# https://leetcode-cn.com/problems/island-perimeter/description/
#
# algorithms
# Easy (66.20%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    18.3K
# Total Submissions: 27.4K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
# 
# 
# 
# 示例 :
# 
# 输入:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# 输出: 16
# 
# 解释: 它的周长是下面图片中的 16 个黄色的边：
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
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
        for r,row in enumerate(grid):
            if ans:
                break
            for c,val in enumerate(row):
                if ans:
                    break
                if val == 1:
                    stack = [(r,c)]
                    seen = {(r,c)}
                    ans = 4
                    while stack:
                        node = stack.pop()
                        for nei in neighbors(*node):
                            if grid[nei[0]][nei[1]] == 1:
                                ans -= 1
                                if nei not in seen:
                                    ans += 4
                                    stack.append(nei)
                                    seen.add((nei))
        return ans
                    

# s = Solution()
# ans = s.islandPerimeter([[0],[1]])
# print(ans)



# @lc code=end

