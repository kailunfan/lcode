#
# @lc app=leetcode.cn id=405 lang=python
#
# [405] 数字转换为十六进制数
#
# https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (50.05%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 23.3K
# Testcase Example:  '26'
#
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
#
# 注意:
#
#
# 十六进制中所有字母(a-f)都必须是小写。
# 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
# 给定的数确保在32位有符号整数范围内。
# 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
#
#
# 示例 1：
#
#
# 输入:
# 26
#
# 输出:
# "1a"
#
#
# 示例 2：
#
#
# 输入:
# -1
#
# 输出:
# "ffffffff"
#
#
#

# @lc code=start


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        key_map = [str(x) for x in range(10)]
        key_map.extend(['a', 'b', 'c', 'd', 'e','f'])
        def deal_positive(n):
            if n == 0:
                return '0'
            ans = []
            while n:
                res, remain = divmod(n, 16)
                ans.append(key_map[remain])
                n = res
            return ''.join(ans[::-1])
            
        mx = 0x100000000
        if num >= 0:
            return deal_positive(num)
        return deal_positive(mx+num)


# @lc code=end
