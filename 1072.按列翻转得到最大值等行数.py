#
# @lc app=leetcode.cn id=1072 lang=python
#
# [1072] 按列翻转得到最大值等行数
#
# https://leetcode-cn.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/
#
# algorithms
# Medium (49.72%)
# Likes:    29
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 3.3K
# Testcase Example:  '[[0,1],[1,1]]'
#
# 给定由若干 0 和 1 组成的矩阵 matrix，从中选出任意数量的列并翻转其上的 每个 单元格。翻转后，单元格的值从 0 变成 1，或者从 1 变为 0
# 。
# 
# 返回经过一些翻转后，行上所有值都相等的最大行数。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[[0,1],[1,1]]
# 输出：1
# 解释：不进行翻转，有 1 行所有值都相等。
# 
# 
# 示例 2：
# 
# 输入：[[0,1],[1,0]]
# 输出：2
# 解释：翻转第一列的值之后，这两行都由相等的值组成。
# 
# 
# 示例 3：
# 
# 输入：[[0,0,0],[0,0,1],[1,1,0]]
# 输出：2
# 解释：翻转前两列的值之后，后两行由相等的值组成。
# 
# 
# 
# 提示：
# 
# 
# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300
# 所有 matrix[i].length 都相等
# matrix[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # 找出特征相同或者相反的行
        # 统计各元素出现的次数
        # [1,0]和[0,1]属于相同元素,转型为其一即可
        # list要转为可hash类型
        counts = defaultdict(int)
        for row in matrix:
            if row[0] == 1:
                for i,item in enumerate(row):
                    row[i] = row[i] ^ 1
            counts[str(row)] += 1
        return max(counts.values())
                
        
# @lc code=end

