#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (36.74%)
# Likes:    5301
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.9M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        max_length = 0
        
        def getPalindrome(lc, rc):
            nonlocal max_length
            nonlocal ans

            while lc>=0 and rc<len(s) and s[lc] == s[rc]:
                lc -= 1
                rc += 1
            lc+=1
            rc-=1
            if rc-lc+1>max_length:
                max_length = rc-lc+1
                ans = s[lc:rc+1]
        
        for i in range(len(s)):
            getPalindrome(i, i)
            if i>0:
                getPalindrome(i-1, i)
        return ans

Solution().longestPalindrome('babad')
        
# @lc code=end

