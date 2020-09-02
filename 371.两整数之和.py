#
# @lc app=leetcode.cn id=371 lang=python
#
# [371] 两整数之和
#
# https://leetcode-cn.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (54.43%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 54.6K
# Testcase Example:  '1\n2'
#
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。
#
# 示例 1:
#
# 输入: a = 1, b = 2
# 输出: 3
#
#
# 示例 2:
#
# 输入: a = -2, b = 3
# 输出: 1
#
#

# @lc code=start


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: intx
        :type b: int
        :rtype: int
        """
        # 不懂
        mx = 0xFFFFFFFF
        a &= mx
        b &= mx
        while b != 0:
            carry = (a & b) << 1 & mx
            a = a ^ b
            b = carry
        return a if a < 0x80000000 else ~(a^mx)


# @lc code=end
