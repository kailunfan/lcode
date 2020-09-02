#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.46%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    87.9K
# Total Submissions: 166.6K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。
#
#
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
#
# 提示：
#
#
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
#
#
#

# @lc code=start


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = 0
        ans = []
        carry = 0
        while True:
            i += 1
            if not carry and i > len(a) and i > len(b):
                break
            if i <= len(a):
                carry += int(a[-i])
            if i <= len(b):
                carry += int(b[-i])
            carry, val = divmod(carry, 2)
            ans.append(val)

        return "".join(str(x) for x in ans[::-1])


# @lc code=end
