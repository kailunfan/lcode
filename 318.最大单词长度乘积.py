#
# @lc app=leetcode.cn id=318 lang=python
#
# [318] 最大单词长度乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (63.04%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 12.2K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j])
# 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
#
# 示例 1:
#
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16
# 解释: 这两个单词为 "abcw", "xtfn"。
#
# 示例 2:
#
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4
# 解释: 这两个单词为 "ab", "cd"。
#
# 示例 3:
#
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0
# 解释: 不存在这样的两个单词。
#
#

# @lc code=start


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        masks = []
        for i in words:
            masks.append(self.get_mask(i))

        ans = 0
        l = len(masks)
        for i in range(l):
            for j in range(i+1, l):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans

    def get_mask(self,word):
        mask = 0
        for w in word:
            mask |= 1 << (ord(w) - ord('a'))
        return mask

# @lc code=end
