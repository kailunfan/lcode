#
# @lc app=leetcode.cn id=187 lang=python
#
# [187] 重复的DNA序列
#
# https://leetcode-cn.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (44.14%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 39.8K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA
# 中的重复序列有时会对研究非常有帮助。
# 
# 编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。
# 
# 
# 
# 示例：
# 
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC", "CCCCCAAAAA"]
# 
#

# @lc code=start
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # BF(超时)
        # n = len(s)
        # ans = []
        # for i in range(n-10+1):
        #     base = s[i:i+10]
        #     for j in range(i+1,n-10+1):
        #         comp = s[j:j+10]
        #         if comp == base:
        #             ans.append(comp)
        #             break
        # return list(set(ans))

        # BF另一种写法(空间换时间)
        L,n = 10,len(s)
        seen,ans = set(),set()
        for i in range(n-L+1):
            if s[i:i+L] not in seen:
                seen.add(s[i:i+L])
            else:
                ans.add(s[i:i+L])
        return list(ans)


# @lc code=end

