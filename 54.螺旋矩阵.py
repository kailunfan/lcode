#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (51.01%)
# Likes:    1737
# Dislikes: 0
# Total Accepted:    568.6K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# -100
#
#
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        res = []
        t,b,l,r = 0,len(matrix)-1, 0, len(matrix[0])-1
        while True:
            # l-r
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t>b:
                break
            # t-b
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            if l>r:
                break
            # r-l
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t>b:
                break
            # b-t
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l>r:
                break
        
        return res

# @lc code=end
