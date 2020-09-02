#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (61.32%)
# Likes:    130
# Dislikes: 0
# Total Accepted:    28.7K
# Total Submissions: 46.4K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。
#
#
#
# 示例:
#
# 输入：
# s = "abcd"
# t = "abcde"
#
# 输出：
# e
#
# 解释：
# 'e' 是那个被添加的字母。
#
#
#

# @lc code=start


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for i in s:
            ans ^= ord(i)
        for i in t:
            ans ^= ord(i)
        return chr(ans)

            
# @lc code=end
