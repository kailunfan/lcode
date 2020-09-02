#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for (index, i) in enumerate(nums):
            remain = target - i
            if remain in nums[index+1:]:
                return [nums.index(i), nums.index(i) + 1 + nums[index+1:].index(remain)]

        return [0, 0]

# @lc code=end


s = Solution()
res = s.twoSum([2,3, 3], 6)
print(res)
