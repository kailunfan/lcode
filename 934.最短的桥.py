#
# @lc app=leetcode.cn id=934 lang=python
#
# [934] 最短的桥
#
# https://leetcode-cn.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (43.59%)
# Likes:    85
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 15.1K
# Testcase Example:  '[[0,1],[1,0]]'
#
# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
#
# 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
#
# 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1。）
#
#
#
# 示例 1：
#
# 输入：[[0,1],[1,0]]
# 输出：1
#
#
# 示例 2：
#
# 输入：[[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#
#
# 示例 3：
#
# 输入：[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1
#
#
#
# 提示：
#
#
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 或 A[i][j] == 1
#
#
#
#
#

# @lc code=start
import collections


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        R = len(A)
        C = len(A[0])

        def get_neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():
            done = set()
            ans = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in done:
                        stack = [(r, c)]
                        seen = {(r, c)}
                        while stack:
                            node = stack.pop()
                            for nei in get_neighbors(*node):
                                if A[nei[0]][nei[1]] and nei not in seen:
                                    stack.append(nei)
                        done |= seen
                        ans.append(seen)
            return ans

        source, target = get_components()

        queue = collections.deque([(node, 0) for node in source])
        done = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target:
                return d-1
            for nei in get_neighbors(*node):
                if nei not in done:
                    queue.append((nei, d+1))
                    done.add(nei)


# @lc code=end
