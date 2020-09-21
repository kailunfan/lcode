#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (65.25%)
# Likes:    205
# Dislikes: 0
# Total Accepted:    25.1K
# Total Submissions: 38.3K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
#
#
# 示例：
# 输入：S = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入：S = "3z4"
# 输出：["3z4", "3Z4"]
#
# 输入：S = "12345"
# 输出：["12345"]
#
#
#
#
# 提示：
#
#
# S 的长度不超过12。
# S 仅由数字和字母组成。
#
#
#

# @lc code=start


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # 迭代
        ans = [S]
        for i in range(len(S)):
            func = None
            if 'a' <= S[i] <= 'z':
                func = 'upper'
            if 'A' <= S[i] <= 'Z':
                func = 'lower'
            if func:
                for a in ans[::]:
                    new_char = getattr(a[i],func)()
                    ans.append(f'{a[:i]}{new_char}{a[i+1:]}')
        return ans

        ans = []
        l = len(S)

        # 回溯
        def backtrack(val, ind):
            ans.append(val)
            for i in range(ind, l):
                if 'a' <= val[i] <= 'z':
                    backtrack(f'{val[:i]}{val[i].upper()}{val[i+1:]}', i+1)
                if 'A' <= val[i] <= 'Z':
                    backtrack(f'{val[:i]}{val[i].lower()}{val[i+1:]}', i+1)
        backtrack(S, 0)
        return ans


# @lc code=end
