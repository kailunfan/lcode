#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (36.92%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    39.9K
# Total Submissions: 107.4K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
#
# 示例1:
#
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
#
#
#
#
# 示例2:
#
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
#
#
#
#
# 注意：
#
#
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
#
#
#

# @lc code=start
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 相同长度区间字符出现次数相同
        if len(s1) > len(s2):
            return False
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for i in range(len(s1)):
            m1[s1[i]] += 1
            m2[s2[i]] += 1

        if m1 == m2:
            return True

        l, r = 0, len(s1)
        while r < len(s2):
            if m2[s2[l]] > 1:
                m2[s2[l]] -= 1
            else:
                m2.pop(s2[l])
            m2[s2[r]] += 1
            if m2 == m1:
                return True
            r += 1
            l += 1
        return False

# @lc code=end
