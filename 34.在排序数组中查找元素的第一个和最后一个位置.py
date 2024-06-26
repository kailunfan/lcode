#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (40.13%)
# Likes:    591
# Dislikes: 0
# Total Accepted:    133K
# Total Submissions: 329.6K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#
from typing import List
# @lc code=start


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        #  get min
        lc = 0
        rc = len(nums) - 1
        while lc < rc:
            m = (lc+rc)//2
            v = nums[m]
            if v < target:
                lc = m+1
            else:
                rc = m

        if nums[lc] != target:
            return [-1, -1]

        min_ind = lc

        #  get max
        lc1, rc1 = lc, len(nums)-1
        while lc1 < rc1:
            m = (lc1+rc1+1)//2
            v = nums[m]
            if v > target:
                rc1 = m-1
            else:
                lc1 = m

        max_ind = lc1
        return [min_ind, max_ind]

# @lc code=end
