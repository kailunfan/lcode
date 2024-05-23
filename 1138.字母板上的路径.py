#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#
# https://leetcode.cn/problems/alphabet-board-path/description/
#
# algorithms
# Medium (51.80%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    26.8K
# Total Submissions: 51.8K
# Testcase Example:  '"leet"'
#
# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。
#
# 在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。
#
#
#
# 我们可以按下面的指令规则行动：
#
#
# 如果方格存在，'U' 意味着将我们的位置上移一行；
# 如果方格存在，'D' 意味着将我们的位置下移一行；
# 如果方格存在，'L' 意味着将我们的位置左移一列；
# 如果方格存在，'R' 意味着将我们的位置右移一列；
# '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
#
#
# （注意，字母板上只存在有字母的位置。）
#
# 返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。
#
#
#
# 示例 1：
#
#
# 输入：target = "leet"
# 输出："DDR!UURRR!!DDD!"
#
#
# 示例 2：
#
#
# 输入：target = "code"
# 输出："RR!DDRR!UUL!R!"
#
#
#
#
# 提示：
#
#
# 1 <= target.length <= 100
# target 仅含有小写英文字母。
#
#
#

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        bx, by = 0, 0
        ans = []
        for c in target:
            diff = ord(c)-ord('a')
            cx, cy = diff % 5, diff // 5
            right = cx - bx
            down = cy - by
            if down < 0:
                ans.append('U'*-down)
            if right < 0:
                ans.append('L'*-right)
            if down > 0:
                ans.append('D'*down)
            if right > 0:
                ans.append('R'*right)
            ans.append('!')
            bx, by = cx, cy
        return ''.join(ans)

# @lc code=end
