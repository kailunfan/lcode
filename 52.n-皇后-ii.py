#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#
# https://leetcode.cn/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.28%)
# Likes:    486
# Dislikes: 0
# Total Accepted:    133.9K
# Total Submissions: 162.7K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
# @lc code=end

