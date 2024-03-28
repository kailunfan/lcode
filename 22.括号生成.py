#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.98%)
# Likes:    1266
# Dislikes: 0
# Total Accepted:    169.8K
# Total Submissions: 223.2K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例：
#
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
#
#
#
from typing import List

# @lc code=start


class Solution:
    def generateParenthesis1(self, n: int) -> List[str]:
        ans = []

        def backtrack(val, lcnt, rcnt):
            if lcnt + rcnt == 2 * n:
                ans.append(val)
            if lcnt < n:
                backtrack(val+"(", lcnt+1, rcnt)
            if rcnt < lcnt:
                backtrack(val+")", lcnt, rcnt+1)
        backtrack('', 0, 0)
        return ans

    # interation
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [("", 0, 0)]
        for i in range(2 * n):
            this_ans = []
            for a in ans:
                if a[1] < n:
                    this_ans.append((a[0]+"(", a[1]+1, a[2]))
                if a[1]>a[2]:
                    this_ans.append((a[0]+")", a[1], a[2]+1))
            ans = this_ans
        return [i[0] for i in ans]

                

        # @lc code=end
