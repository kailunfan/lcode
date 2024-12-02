#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.95%)
# Likes:    1199
# Dislikes: 0
# Total Accepted:    326.7K
# Total Submissions: 847.6K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
from typing import List
# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        ans = ''
        min_length = min(len(i) for i in strs)
        for i in range(min_length):
            v0 = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != v0:
                    return ans
            ans += v0
        return ans
# @lc code=end
