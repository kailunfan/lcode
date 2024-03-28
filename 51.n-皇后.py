#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode.cn/problems/n-queens/description/
#
# algorithms
# Hard (73.94%)
# Likes:    1976
# Dislikes: 0
# Total Accepted:    349.3K
# Total Submissions: 472.4K
# Testcase Example:  '4'
#
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#
#
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[["Q"]]
#
#
#
#
# 提示：
#
#
# 1 <= n <= 9
#
#
#
#
#
from typing import List
# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [[]]
        for _ in range(n):
            this_ans = []
            for a in ans:
                for ni in range(n):
                    if self.validate(a, ni):
                        v = ["."]*n
                        v[ni] = 'Q'
                        # 判断是否满足条件
                        this_ans.append([*a, ''.join(v)])
            ans = this_ans
        return ans

    def validate(self, line_list, new_ind):
        for line_no, line in enumerate(line_list):
            if line[new_ind] == 'Q':
                return False
            # 左上
            j = new_ind - len(line_list) + line_no
            if j >= 0 and line[j] == 'Q':
                return False
            # 右上
            j = new_ind + len(line_list) - line_no
            if j < len(line) and line[j] == 'Q':
                return False
        return True


print(Solution().solveNQueens(4))
# print(Solution().validate([".Q..","...Q","Q..."],2))

# @lc code=end
