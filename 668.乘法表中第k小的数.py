#
# @lc app=leetcode.cn id=668 lang=python
#
# [668] 乘法表中第k小的数
#
# https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/description/
#
# algorithms
# Hard (46.81%)
# Likes:    87
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 6.3K
# Testcase Example:  '3\n3\n5'
#
# 几乎每一个人都用 乘法表。但是你能在乘法表中快速找到第k小的数字吗？
#
# 给定高度m 、宽度n 的一张 m * n的乘法表，以及正整数k，你需要返回表中第k 小的数字。
#
# 例 1：
#
#
# 输入: m = 3, n = 3, k = 5
# 输出: 3
# 解释:
# 乘法表:
# 1    2    3
# 2    4    6
# 3    6    9
#
# 第5小的数字是 3 (1, 2, 2, 3, 3).
#
#
# 例 2：
#
#
# 输入: m = 2, n = 3, k = 6
# 输出: 6
# 解释:
# 乘法表:
# 1    2    3
# 2    4    6
#
# 第6小的数字是 6 (1, 2, 2, 3, 4, 6).
#
#
# 注意：
#
#
# m 和 n 的范围在 [1, 30000] 之间。
# k 的范围在 [1, m * n] 之间。
#
#
#

# @lc code=start


class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def leCount(val):
            count = 0
            for i in range(1, m+1):
                count += min(n, val//i)
            return count
            
        lo, hi = 1, m*n
        while lo < hi:
            mi = (lo+hi) // 2
            if leCount(mi) < k:
                lo = mi + 1
            else:
                hi = mi
        return lo


# @lc code=end
