#
# @lc app=leetcode.cn id=399 lang=python
#
# [399] 除法求值
#
# https://leetcode-cn.com/problems/evaluate-division/description/
#
# algorithms
# Medium (53.57%)
# Likes:    147
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 15.1K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
'[2.0,3.0]\n' +
'[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# 给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k
# 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。
#
# 示例 :
# 给定 a / b = 2.0, b / c = 3.0
# 问题:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# 返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]
#
# 输入为:  vector<pair<string, string>> equations, vector<double>& values,
# vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() ==
# values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。
# 返回vector<double>类型。
#
# 基于上述例子，输入如下：
#
# equations(方程式) = [ ["a", "b"], ["b", "c"] ],
# values(方程式结果) = [2.0, 3.0],
# queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ].
#
#
# 输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。
#
#

# @lc code=start


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        from collections import defaultdict
        graph = defaultdict(dict)
        for e, v in zip(equations, values):
            graph[e[0]][e[1]] = v
            graph[e[1]][e[0]] = 1/v

        def dfs(s, t):
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                if node not in visited:
                    visited.add(node)
                    this_val = dfs(node, t)
                    if this_val != -1:
                        return this_val * graph[s][node]
            return -1

        ans = []
        for i in queries:
            visited = set()
            ans.append(dfs(i[0], i[1]))
        return ans


# @lc code=end
