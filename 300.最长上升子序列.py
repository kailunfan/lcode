#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (44.18%)
# Likes:    779
# Dislikes: 0
# Total Accepted:    109.3K
# Total Submissions: 245.2K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#

# @lc code=start


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        if not nums:
            return 0
        L = len(nums)
        state = [1] * L
        for i in range(L):
            for j in range(i):
                if nums[i] > nums[j]:
                    state[i] = max(state[i], state[j]+1)
        return max(state)
        
# @lc code=end
