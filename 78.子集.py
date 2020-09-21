#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (77.16%)
# Likes:    593
# Dislikes: 0
# Total Accepted:    95.2K
# Total Submissions: 123K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

# @lc code=start


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯
        ans = []
        l = len(nums)
        def search(target,ind):
            ans.append(target)
            for i in range(ind,l):
                search(target+[nums[i]],i+1)
        search([],0)
        return ans

        # 逐个元素添加
        ans = [[]]
        for i in nums:
            ans += [x+[i] for x in ans]
        return ans

        # 二进制掩码
        ans = []
        l = len(nums)
        max_bit = 1 << l
        for i in range(max_bit):
            mask = bin(i | max_bit)[3:]
            ans.append([nums[x] for x in range(l) if mask[x] == '1'])
        return ans


# @lc code=end
