#
# @lc app=leetcode.cn id=201 lang=python
#
# [201] 数字范围按位与
#
# https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (44.65%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 27.4K
# Testcase Example:  '5\n7'
#
# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
#
# 示例 1: 
#
# 输入: [5,7]
# 输出: 4
#
# 示例 2:
#
# 输入: [0,1]
# 输出: 0
#
#

# @lc code=start


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        # 分析规律(已经很骄傲了,MD)
        # ans = 0
        # gap = n - m + 1
        # l = len(bin(n))-2
        # for i in range(0, l):
        #     if gap > 2**i:
        #         continue
        #     m_is_1 = m % (2 ** (i+1)) >= 2 ** i
        #     n_is_1 = n % (2 ** (i+1)) >= 2 ** i
        #     if m_is_1 and n_is_1:
        #         ans += 1 << i
        # return ans

        # m--n的公共前缀===m,n的公共前缀
        ans = 0
        move = 0
        while m != n:
            m >>= 1
            n >>= 1
            move += 1
        return m << move


# @lc code=end
