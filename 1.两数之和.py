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
        map = {i: ind for ind, i in enumerate(nums)}
        for (index, i) in enumerate(nums):
            remain = target - i
            v = map.get(remain)
            if not v:
                continue
            # 容易忽略的点
            if v == index:
                continue
            return [index, map[remain]]

        return [0, 0]

# @lc code=end


s = Solution()
res = s.twoSum([3, 2, 4], 6)
print(res)
