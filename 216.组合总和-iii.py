#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (71.62%)
# Likes:    153
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 39.6K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 
# 说明：
# 
# 
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
# 
# 示例 2:
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 迭代
        res = [[]]
        for i in range(1,10):
            res += [x+[i] for x in res if len(x)<k and sum(x)<=n]
        return [x for x in res if sum(x)==n and len(x)==k]

        # 回溯
        ans = []
        def backtrack(val,ind):
            s = sum(val)
            if s > n:
                return
            if len(val) == k and s==n:
                return ans.append(val)
            for i in range(ind,10):
                backtrack([i]+val,i+1)
        backtrack([],1)
        return ans

# @lc code=end

