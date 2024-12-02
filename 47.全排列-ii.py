#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (58.08%)
# Likes:    312
# Dislikes: 0
# Total Accepted:    63.1K
# Total Submissions: 107K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#

# @lc code=start
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        # 不懂
        def backtrack(ind):
            if ind == len(nums):
                ans.append(nums[:])
                return
            for i in range(ind, len(nums)):
                if used[i]:
                    continue
                if i>ind and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                nums[i],nums[ind] = nums[ind],nums[i]
                backtrack(ind+1)
                nums[i],nums[ind] = nums[ind],nums[i]
                used[i] = False
         
        ans = []
        nums.sort()
        backtrack(0)
        return ans

# @lc code=end
