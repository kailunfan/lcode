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
        result = []
        def backtrack(ind):
            if ind == len(nums):
                result.append(nums[:])
            for i in range(ind, len(nums)):
                nums[ind],nums[i] = nums[i],nums[ind] 
                backtrack(ind+1)
                nums[ind],nums[i] = nums[i],nums[ind] 
        backtrack(0)
        return result

    # iteration
    def permute1(self, nums):
        ans = [[]]
        for n in nums:
            this_ans = []
            for l in ans:
                for i in range(0, len(l)+1):
                    this_ans.append([*l[:i], n, *l[i:]])
            ans = this_ans
        return ans

# @lc code=end
