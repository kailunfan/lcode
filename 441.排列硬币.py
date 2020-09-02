#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#
# https://leetcode-cn.com/problems/arranging-coins/description/
#
# algorithms
# Easy (40.49%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 55.2K
# Testcase Example:  '5'
#
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
#
# 给定一个数字 n，找出可形成完整阶梯行的总行数。
#
# n 是一个非负整数，并且在32位有符号整型的范围内。
#
# 示例 1:
#
#
# n = 5
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤
#
# 因为第三行不完整，所以返回2.
#
#
# 示例 2:
#
#
# n = 8
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# 因为第四行不完整，所以返回3.
#
#
#

# @lc code=start


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 常规
        # i = 0
        # total = 0
        # while True:
        #     if total + i + 1 > n:
        #         break
        #     i += 1
        #     total = total + i
        # return i

        # 数学
        # i = 0
        # while i*(i+1)/2 <= n:
        #     i += 1
        # return i - 1

        # 二分查找
        # 找到第一个大于n的左边
        if n <= 1:
            return n
        l = 1
        r = n
        while l < r:
            m = (l+r) // 2
            if self.calc(m) > n:
                r = m
            else:
                l = m+1
        return l-1

    def calc(self, k):
        return (1+k) * k / 2

# @lc code=end
