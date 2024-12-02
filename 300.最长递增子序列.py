#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# https://leetcode.cn/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (55.79%)
# Likes:    3653
# Dislikes: 0
# Total Accepted:    958.5K
# Total Submissions: 1.7M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
# 的子序列。
#
#
# 示例 1：
#
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
#
# 示例 3：
#
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：
#
#
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#
#
#

# @lc code=start
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        state = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    state[i] = max(state[i], state[j]+1)
        return max(state)
