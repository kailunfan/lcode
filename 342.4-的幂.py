#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (48.49%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 52.9K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
#
#
# 示例 2:
#
# 输入: 5
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#

# @lc code=start


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        mask = 0xaaaaaaaa
        return num > 0 and num & (num-1) == 0 and mask & num == 0

# @lc code=end
