#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (74.76%)
# Likes:    739
# Dislikes: 0
# Total Accepted:    137.6K
# Total Submissions: 180.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

import collections
import copy

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 迭代
        tmp = [[]]
        for i in nums:
            tmp += [t+[i] for t in tmp]
            print(tmp)
        return [x for x in tmp if len(tmp)==len(nums)]    

        # 标准回溯
        result = []
        visited = [False] * len(nums)
        def backtrack(tmp):
            if len(tmp) == len(nums):
                result.append(tmp)
                return 
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                backtrack(tmp + [nums[i]])
                visited[i] = False
            return result
        return backtrack([])


        ans = []
        l = len(nums)
        # 回溯
        def check(this_ans):
            if len(this_ans) == l:
                ans.append(this_ans[:])
            for i in nums:
                if i not in this_ans:
                    this_ans.append(i)
                    check(this_ans)
                    this_ans.pop()
        check([])
        return ans
            
# @lc code=end



