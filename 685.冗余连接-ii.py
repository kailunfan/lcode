#
# @lc app=leetcode.cn id=685 lang=python
#
# [685] 冗余连接 II
#
# https://leetcode-cn.com/problems/redundant-connection-ii/description/
#
# algorithms
# Hard (33.87%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    3K
# Total Submissions: 8.6K
# Testcase Example:  '[[1,2],[1,3],[2,3]]'
#
# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。
#
# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N)
# 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
#
# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u and
# v和顶点的边，其中父节点u是子节点v的一个父节点。
#
# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。
#
# 示例 1:
#
#
# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
# ⁠ 1
# ⁠/ \
# v   v
# 2-->3
#
#
# 示例 2:
#
#
# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
# ⁠    ^    |
# ⁠    |    v
# ⁠    4 <- 3
#
#
# 注意:
#
#
# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。
#
#
#
from collections import defaultdict
import copy
# @lc code=start


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        origin_ancestors = {}

        # 构造邻接表和入度表
        indegrees = defaultdict(int)
        from_edges = defaultdict(list)

        for f, t in edges:
            origin_ancestors[f] = f
            origin_ancestors[t] = t
            from_edges[t].append([f, t])
            indegrees[t] += 1

        def get_ancestor(key):
            if key == ancestors[key]:
                return key
            return get_ancestor(ancestors[key])

        # 情况1:有入度大于1的点

        # 找到入度大于1的节点,结果必在其临边中
        for key, idgr in indegrees.items():
            if idgr <= 1:
                continue
            # 去掉一条冗余边,判断剩余是否成环
            remove_edge = from_edges[key][-1]
            ancestors = origin_ancestors
            for f, t in edges:
                if [f, t] == remove_edge:
                    continue
                f_anc = get_ancestor(f)
                t_anc = get_ancestor(t)
                # 成环了,结果为另外一条边
                if f_anc == t_anc:
                    return from_edges[key][0]
                ancestors[t_anc] = f_anc
            # 没有成环,结果为当前边
            return remove_edge

        # 情况2:没有入度大于1的边,直接找成环的边.此时问题退化到无向图;
        ancestors = origin_ancestors
        for f, t in edges:
            f_anc = get_ancestor(f)
            t_anc = get_ancestor(t)
            print(f, t, f_anc, t_anc)
            if f_anc == t_anc:
                return [f, t]
            ancestors[t_anc] = f_anc


# @lc code=end
