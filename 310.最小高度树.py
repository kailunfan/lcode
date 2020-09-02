#
# @lc app=leetcode.cn id=310 lang=python
#
# [310] 最小高度树
#
# https://leetcode-cn.com/problems/minimum-height-trees/description/
#
# algorithms
# Medium (33.78%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 24.4K
# Testcase Example:  '4\n[[1,0],[1,2],[1,3]]'
#
#
# 对于一个具有树特征的无向图，我们可选择任何一个节点作为根。图因此可以成为树，在所有可能的树中，具有最小高度的树被称为最小高度树。给出这样的一个图，写出一个函数找到所有的最小高度树并返回他们的根节点。
#
# 格式
#
# 该图包含 n 个节点，标记为 0 到 n - 1。给定数字 n 和一个无向边 edges 列表（每一个边都是一对标签）。
#
# 你可以假设没有重复的边会出现在 edges 中。由于所有的边都是无向边， [0, 1]和 [1, 0] 是相同的，因此不会同时出现在 edges 里。
#
# 示例 1:
#
# 输入: n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
# ⁠       0
# ⁠       |
# ⁠       1
# ⁠      / \
# ⁠     2   3
#
# 输出: [1]
#
#
# 示例 2:
#
# 输入: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
# ⁠    0  1  2
# ⁠     \ | /
# ⁠       3
# ⁠       |
# ⁠       4
# ⁠       |
# ⁠       5
#
# 输出: [3, 4]
#
# 说明:
#
#
# 根据树的定义，树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。
# 树的高度是指根节点和叶子节点之间最长向下路径上边的数量。
#
#
#

# @lc code=start

from collections import defaultdict, deque


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 思路:
        # 从最外层遍历,最后一层即为结果.
        
        if n == 1:
            return [0]

        # 构造邻接表和度
        adjs = defaultdict(list)
        degrees = [0 for _ in range(n)]
        for (f, t) in edges:
            adjs[f].append(t)
            adjs[t].append(f)
            degrees[f] += 1
            degrees[t] += 1

        # BFS
        # 第一层(最外层)
        layer = []
        for ind, val in enumerate(degrees):
            if val == 1:
                layer.append(ind)
        # 层层缩进:遍历当前层,确定下一层节点.
        while layer:
            next_layer = []
            for node in layer:
                for neighbor in adjs[node]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        next_layer.append(neighbor)
            if not next_layer:  # 下一层没东西了,说明当前遍历的最后一层,也就是我们需要的
                return layer
            layer = next_layer

# @lc code=end
