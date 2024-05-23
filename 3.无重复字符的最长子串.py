#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (38.81%)
# Likes:    7677
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 4.6M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
# 示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        st = set()
        lc, rc = 0, 0
        while lc < len(s):
            while rc < len(s):
                if s[rc] in st:
                    break
                st.add(s[rc])
                rc += 1
            ans = max(ans, rc-lc)
            if s[lc] in st:
                st.remove(s[lc])
            lc += 1
        return ans


# @lc code=end
