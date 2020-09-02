#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (43.29%)
# Likes:    239
# Dislikes: 0
# Total Accepted:    135.1K
# Total Submissions: 295.5K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
# 示例 2:
#
# 输入: "race a car"
# 输出: false
#
#
#

# @lc code=start


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.s = s
        lc = 0
        rc = len(s) - 1
        while lc < rc:
            while lc<len(s) and not self.valid(lc):
                lc += 1
            while rc>=0 and not self.valid(rc):
                rc -= 1
            if lc>=rc:
                return True
            if not self.compare(lc, rc):
                return False
            lc += 1
            rc -= 1
        return True

    def valid(self,pos):
        if self.s[pos].isalnum():
            return True
        return False

    def compare(self,lc, rc):
        lv = ord(self.s[lc])
        rv = ord(self.s[rc])
        if 97 <= lv <= 122:
            lv -= 32
        if 97 <= rv <= 122:
            rv -= 32
        return lv == rv

r = Solution().isPalindrome(".,")
print(r)


# @lc code=end
