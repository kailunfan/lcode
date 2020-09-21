#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#
# https://leetcode-cn.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (52.32%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    13K
# Total Submissions: 24.8K
# Testcase Example:  '4'
#
# 泰波那契序列 Tn 定义如下： 
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
#
#
#
# 示例 1：
#
# 输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
#
# 示例 2：
#
# 输入：n = 25
# 输出：1389537
#
#
#
#
# 提示：
#
#
# 0 <= n <= 37
# 答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
#
#
#

# @lc code=start


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1
        t0, t1, t2 = 0, 1, 1
        for i in range(n-2):
            t0, t1, t2 = t1, t2, t0+t1+t2
        return t2

# @lc code=end
