#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#
# https://leetcode.cn/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (54.91%)
# Likes:    853
# Dislikes: 0
# Total Accepted:    97.1K
# Total Submissions: 176.7K
# Testcase Example:  '"ABAB"\n2'
#
# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
# 
# 在执行上述操作后，返回 包含相同字母的最长子字符串的长度。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
# 可能存在其他的方法来得到同样的结果。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 仅由大写英文字母组成
# 0 <= k <= s.length
# 
# 
#
from collections import defaultdict
# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 不会啊
        m = defaultdict(int)
        n = len(s)
        maxn = left = right = 0
        while right<n:
            m[s[right]]+=1
            maxn = max(maxn, m[s[right]])
            if right-left+1-maxn>k:
                m[s[left]] -= 1
                left += 1
            right += 1
        return right - left


        
# @lc code=end

