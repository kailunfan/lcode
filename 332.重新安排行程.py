#
# @lc app=leetcode.cn id=332 lang=python
#
# [332] 重新安排行程
#
# https://leetcode-cn.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (36.57%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 21K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# 给定一个机票的字符串二维数组 [from,
# to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从
# JFK 出发。
# 
# 说明:
# 
# 
# 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"]
# 相比就更小，排序更靠前
# 所有的机场都用三个大写字母表示（机场代码）。
# 假定所有机票至少存在一种合理的行程。
# 
# 
# 示例 1:
# 
# 输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# 示例 2:
# 
# 输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
# 
#

# @lc code=start
from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 构造邻接表
        d = defaultdict(list)
        for (fr,to) in tickets:
            d[fr].append(to)
        for v in d.values():
            v.sort()
        ans = []
        # 深度遍历的过程中会改变d[f]的值,这时候就对广度方向进行了剪枝,避免重复访问到;
        # 相当于将访问过的元素从邻接表中删除.
        def dfs(f):
            while d[f]:
                dfs(d[f].pop(0))
            ans.insert(0,f)
        dfs('JFK')
        return ans
        
        
        
# @lc code=end

