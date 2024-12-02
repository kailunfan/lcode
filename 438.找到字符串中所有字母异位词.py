#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (53.39%)
# Likes:    1546
# Dislikes: 0
# Total Accepted:    551.2K
# Total Submissions: 1M
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
# 
# 
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 统计p
        # 定窗口,统计w,记录相同个数
        # 滑动窗口
        p_wc = defaultdict(int)
        s_wc = defaultdict(int)
        same_count = 0
        target_count = len(p)
        ans = 0
        for c in p:
            p_wc[c] += 1
        
        for i in range(0, len(p)):
            s_wc[s[i]] += 1
        
        for k in p_wc.keys():
            if s_wc[k] == p_wc[k]:
                same_count += 1
        if same_count == target_count:
            ans += 1
        
        for i in range(len(p),len(s)-len(p)):
            v_start = s[i]
            v_end = s[i+len(p)]
            s_wc[v_start] -= 1
            s_wc[v_end] += 1
            if v_start in p_wc and p_wc[v_start] == s_wc[v_start]:
                same_count += 1
            if v_end in p_wc and p_wc[v_end] == s_wc[v_end]:
                same_count += 1
        

        
        
# @lc code=end

