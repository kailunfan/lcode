#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode.cn/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (70.87%)
# Likes:    1318
# Dislikes: 0
# Total Accepted:    450.5K
# Total Submissions: 636.2K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[[1]]
#
#
#
#
# 提示：
#
#
# 1
#
#
#
from typing import List
# @lc code=start


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n-1, 0, n-1
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n*n
        
        def fill_num():
            nonlocal num
            num += 1
            return num - 1
        
        while num <= tar:
            for i in range(l, r+1):
                ans[t][i] = fill_num()
            t += 1

            for i in range(t, b+1):
                ans[i][r] = fill_num()
            r -= 1

            for i in range(r, l-1, -1):
                ans[b][i] = fill_num()
            b -= 1

            for i in range(b, t-1, -1):
                ans[i][l] = fill_num()
            l += 1
        return ans
    
    
# @lc code=end
