#
# @lc app=leetcode.cn id=46 lang=python3
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

        # 标准回溯
        result = []
        def backtrack(tmp,visited):
            if len(tmp) == len(nums):
                result.append(tmp)
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = 1
                backtrack(tmp + [nums[i]],visited)
                visited[i] = 0
        backtrack([],[0]*len(nums))
        return result
            
# @lc code=end

