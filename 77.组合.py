#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (73.52%)
# Likes:    325
# Dislikes: 0
# Total Accepted:    66K
# Total Submissions: 88.6K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 迭代
        ans = [[]]
        for i in range(1,n+1):
            ans += [x+[i] for x in ans if len(x)<k]
        return [x for x in ans if len(x) == k]
        
        # 回溯
        ans = []
        def backtrack(val,ind):
            if len(val) == k:
                ans.append(val)
            for i in range(ind+1,n+1):
                backtrack(val+[i],i)
        backtrack([],0)
        return ans

# @lc code=end

