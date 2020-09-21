#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (60.69%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    46K
# Total Submissions: 75.7K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 回溯
        ans = []
        nums.sort()

        def search(val, ind):
            ans.append(val)
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                search(val+[nums[i]], i+1)
        search([], 0)
        return ans


# @lc code=end
