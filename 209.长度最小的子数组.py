#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.39%)
# Likes:    447
# Dislikes: 0
# Total Accepted:    88.1K
# Total Submissions: 198.7K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续
# 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
#
#
#
# 示例：
#
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
#
#
# 进阶：
#
#
# 如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#
#

# @lc code=start


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        # 双指针一次遍历
        # 滑动窗口
        ans = float('inf')
        lc, rc = 0, 0

        sm = nums[0]
        while rc < len(nums):
            if sm >= s:
                ans = min(ans, rc-lc+1)
                sm -= nums[lc]
                lc += 1
            else:
                rc += 1
                # 关键点,处理下标越界
                if rc >= len(nums):
                    break
                sm += nums[rc]
        return ans if ans != float('inf') else 0

        #  暴力解法
        ans = float('inf')
        for i in range(len(nums)):
            n = 0
            sm = 0
            for j in range(i, len(nums)):
                sm += nums[j]
                n += 1
                if sm >= s:
                    ans = min(ans, n)
                    break
        return ans if ans != float('inf') else 0


# @lc code=end
