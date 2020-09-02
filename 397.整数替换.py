#
# @lc app=leetcode.cn id=397 lang=python
#
# [397] 整数替换
#
# https://leetcode-cn.com/problems/integer-replacement/description/
#
# algorithms
# Medium (34.83%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    7K
# Total Submissions: 19.8K
# Testcase Example:  '8'
#
# 给定一个正整数 n，你可以做如下操作：
#
# 1. 如果 n 是偶数，则用 n / 2替换 n。
# 2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
# n 变为 1 所需的最小替换次数是多少？
#
# 示例 1:
#
#
# 输入:
# 8
#
# 输出:
# 3
#
# 解释:
# 8 -> 4 -> 2 -> 1
#
#
# 示例 2:
#
#
# 输入:
# 7
#
# 输出:
# 4
#
# 解释:
# 7 -> 8 -> 4 -> 2 -> 1
# 或
# 7 -> 6 -> 3 -> 2 -> 1
#
#
#

# @lc code=start
from collections import deque


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 广度优先搜索
        queue = deque([(n, 0)])
        while queue:
            cur, dep = queue.popleft()
            if cur == 1:
                return dep
            if cur % 2 == 0:
                queue.append((cur/2, dep+1))
            else:
                queue.extend([(cur+1, dep+1), (cur-1, dep+1)])


# @lc code=end
