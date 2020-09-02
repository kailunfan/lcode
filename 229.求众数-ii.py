#
# @lc app=leetcode.cn id=229 lang=python
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (42.98%)
# Likes:    192
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 36.5K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# 
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: [3]
# 
# 示例 2:
# 
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]
# 
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 摩尔投票法
        if not nums or len(nums) == 1:
            return nums
        c1,c2 = nums[0],nums[0]
        n1,n2 = 0,0
        for i in nums:
            if i == c1:
                n1 += 1
                continue
            if i == c2:
                n2 += 1
                continue
            if n1 == 0:
                c1 = i
                n1 = 1
                continue
            if n2 == 0:
                c2 = i
                n2 = 1
                continue
            n1 -= 1
            n2 -= 1
        return list({i for i in [c1,c2] if nums.count(i) > len(nums) / 3})
            

# @lc code=end

