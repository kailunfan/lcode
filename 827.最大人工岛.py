#
# @lc app=leetcode.cn id=827 lang=python
#
# [827] 最大人工岛
#
# https://leetcode-cn.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (39.59%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    2.3K
# Total Submissions: 5.6K
# Testcase Example:  '[[1,0],[0,1]]'
#
# 在二维地图上， 0代表海洋， 1代表陆地，我们最多只能将一格 0 海洋变成 1变成陆地。
#
# 进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 1 可形成岛屿）
#
# 示例 1:
#
#
# 输入: [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
#
#
# 示例 2:
#
#
# 输入: [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。
#
# 示例 3:
#
#
# 输入: [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。
#
# 说明:
#
#
# 1 <= grid.length = grid[0].length <= 50
# 0 <= grid[i][j] <= 1
#
#
#

# @lc code=start


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])

        def neighbors(r, c):
            for nr, nc in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        # 深度优先搜索获取所有的岛屿
        lands = []
        seen = set()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if not val or (r, c) in seen:
                    continue
                # 新的岛屿
                stack = [(r, c)]
                this_land = {(r, c)}
                while stack:
                    node = stack.pop()
                    for new_node in neighbors(*node):
                        if grid[new_node[0]][new_node[1]] and new_node not in this_land:
                            this_land.add(new_node)
                            stack.append(new_node)
                lands.append(this_land)
                seen |= this_land

        # print(lands)

        # 找0,找0周围的岛屿
        has_ocean = False
        ans = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    has_ocean = True
                    this_neighbors = {x for x in neighbors(r, c)}
                    neighbor_land_ids = set()
                    for ind,land in enumerate(lands):
                        if not land.isdisjoint(this_neighbors):
                            neighbor_land_ids.add(ind)
                    this_ans = sum([len(lands[x]) for x in neighbor_land_ids]) + 1
                    ans = max(ans, this_ans)
        if not has_ocean:
            return len(lands[0])
        return ans

# s = [[1, 0], [0, 1]]
# s =  [[1, 1], [1, 0]]
# s = [[1, 1], [1, 1]]
# print(Solution().largestIsland(s))
# @lc code=end
