#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (45.44%)
# Likes:    543
# Dislikes: 0
# Total Accepted:    172.9K
# Total Submissions: 378.4K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
#
#
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
#
#
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
#
#
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
#
#
#

# @lc code=start


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # lo = 0
        # hi = len(nums)
        # while lo < hi:
        #     mid = (lo+hi) // 2
        #     if nums[mid] < target:
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # return lo

        # 模式解法
        # 1. <=
        # 2. m+1,m-1
        # 3. 根据题目要求返回位置.
        # l, h = 0, len(nums) - 1
        # while l <= h:
        #     m = (l+h) // 2
        #     if nums[m] >= target:
        #         if m == 0 or nums[m-1] < target:
        #             return m
        #         h = m - 1
        #     else:
        #         l = m + 1
        # return l

        # 模式简化下
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                h = mid-1
        return l


# @lc code=end
