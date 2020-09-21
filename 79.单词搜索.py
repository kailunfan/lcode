#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (42.34%)
# Likes:    616
# Dislikes: 0
# Total Accepted:    108.8K
# Total Submissions: 249.8K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
# 提示：
#
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#

# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(pos, i, j, visited):
            if pos == len(word):
                return True
            for mx, my in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x_ind = i + mx
                y_ind = j + my
                if 0 <= x_ind < len(board) and 0 <= y_ind < len(board[0]):
                    if board[x_ind][y_ind] == word[pos] and (x_ind,y_ind) not in visited:
                        visited.add((x_ind,y_ind))
                        tmp_res = search(pos+1, x_ind, y_ind,visited)
                        visited.remove((x_ind,y_ind))
                        if tmp_res:
                            return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(1, i, j, {(i, j)}):
                        return True
        return False


# @lc code=end

["a", "a", "a", "a"],
["a", "a", "a", "a"],
["a", "a", "a", "a"]
